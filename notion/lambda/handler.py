import logging
import os
from datetime import date, timedelta

from notion_client import Client

logger = logging.getLogger()
logger.setLevel(logging.INFO)

notion = Client(auth=os.environ["NOTION_TOKEN"])
AUTOMATIONS_DB_ID = os.environ["NOTION_AUTOMATIONS_DB_ID"]
TASKS_DB_ID = os.environ["NOTION_TASKS_DB_ID"]

PRIORITY_RANK = {"P3": 0, "P2": 1, "P1": 2}
DONE_STATUS = "Done 🙌"


# ---------------------------------------------------------------------------
# Notion helpers
# ---------------------------------------------------------------------------


def query_all(database_id, filter_obj=None):
    """Paginate through all results from a database query."""
    results = []
    kwargs = {"database_id": database_id}
    if filter_obj:
        kwargs["filter"] = filter_obj
    while True:
        resp = notion.databases.query(**kwargs)
        results.extend(resp["results"])
        if not resp.get("has_more"):
            break
        kwargs["start_cursor"] = resp["next_cursor"]
    return results


def prop_text(page, name):
    p = page["properties"].get(name, {})
    items = p.get("rich_text") or p.get("title") or []
    return items[0]["plain_text"] if items else None


def prop_number(page, name):
    p = page["properties"].get(name, {})
    return p.get("number")


def prop_select(page, name):
    p = page["properties"].get(name, {})
    s = p.get("select")
    return s["name"] if s else None


def prop_checkbox(page, name):
    p = page["properties"].get(name, {})
    return p.get("checkbox", False)


def prop_date(page, name):
    """Return the created_time date for system props, or start date for date props."""
    p = page["properties"].get(name, {})
    if p.get("type") == "created_time":
        val = p.get("created_time", "")
    else:
        d = p.get("date") or {}
        val = d.get("start", "")
    return date.fromisoformat(val[:10]) if val else None


def last_touched(page):
    for key, val in page["properties"].items():
        if val.get("type") == "last_edited_time":
            t = val.get("last_edited_time", "")
            return date.fromisoformat(t[:10]) if t else None
    return None


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------


def compute_target_priority(automation, days_since_creation):
    p2 = prop_number(automation, "escalate_p2_after_days")
    p1 = prop_number(automation, "escalate_p1_after_days")
    if p1 is not None and days_since_creation >= p1:
        return "P1"
    if p2 is not None and days_since_creation >= p2:
        return "P2"
    return "P3"


def maybe_escalate(task, automation, today):
    """Escalate based on Date Created. Used by monthly and escalation_only.
    after_completion uses period as cycle start instead (see handle_after_completion)."""
    status = prop_select(task, "Status")
    if status == DONE_STATUS:
        return
    created = prop_date(task, "Date Created")
    if not created:
        return
    days = (today - created).days
    target = compute_target_priority(automation, days)
    current_rank = PRIORITY_RANK.get(status, 0)
    target_rank = PRIORITY_RANK.get(target, 0)
    if target_rank > current_rank:
        notion.pages.update(
            page_id=task["id"],
            properties={"Status": {"select": {"name": target}}},
        )
        name = prop_text(task, "Name")
        logger.info(f"Escalated '{name}' from {status} → {target}")


def create_task(automation, period, today):
    automation_id = automation["id"]
    template = prop_text(automation, "task_name_template") or prop_text(automation, "Name")
    name = format_name(template, period, today)
    initial = compute_target_priority(automation, 0)
    notion.pages.create(
        parent={"database_id": TASKS_DB_ID},
        properties={
            "Name": {"title": [{"text": {"content": name}}]},
            "Status": {"select": {"name": initial}},
            "automation_id": {"rich_text": [{"text": {"content": automation_id}}]},
            "period": {"rich_text": [{"text": {"content": period}}]},
        },
    )
    logger.info(f"Created task '{name}' (automation={automation_id}, period={period})")


def format_name(template, period, today):
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    return template.format(
        month_name=month_names[today.month - 1],
        month_short=month_names[today.month - 1][:3],
        month_num=f"{today.month:02d}",
        year=today.year,
        year_short=str(today.year)[2:],
        period=period,
        date=today.isoformat(),
    )


# ---------------------------------------------------------------------------
# Per-type handlers
# ---------------------------------------------------------------------------


def handle_monthly(automation, today):
    create_on_day = prop_number(automation, "create_on_day")
    if create_on_day is None:
        logger.warning(f"monthly automation {automation['id']} missing create_on_day")
        return

    period = today.strftime("%Y-%m")
    existing = query_all(
        TASKS_DB_ID,
        {
            "and": [
                {"property": "automation_id", "rich_text": {"equals": automation["id"]}},
                {"property": "period", "rich_text": {"equals": period}},
            ]
        },
    )

    if existing:
        maybe_escalate(existing[0], automation, today)
    elif today.day == int(create_on_day):
        create_task(automation, period, today)


def handle_after_completion(automation, today):
    recurrence_days = prop_number(automation, "recurrence_days")
    if recurrence_days is None:
        logger.warning(f"after_completion automation {automation['id']} missing recurrence_days")
        return

    existing = query_all(
        TASKS_DB_ID,
        {"property": "automation_id", "rich_text": {"equals": automation["id"]}},
    )

    if not existing:
        create_task(automation, today.isoformat(), today)
        return

    task = existing[0]
    status = prop_select(task, "Status")

    if status != DONE_STATUS:
        # Use period as cycle start date for escalation (survives resets)
        cycle_start_raw = prop_text(task, "period")
        try:
            cycle_start = date.fromisoformat(cycle_start_raw) if cycle_start_raw else None
        except ValueError:
            cycle_start = None
        if cycle_start:
            days = (today - cycle_start).days
            target = compute_target_priority(automation, days)
            current_rank = PRIORITY_RANK.get(status, 0)
            if PRIORITY_RANK.get(target, 0) > current_rank:
                notion.pages.update(
                    page_id=task["id"],
                    properties={"Status": {"select": {"name": target}}},
                )
                name = prop_text(task, "Name")
                logger.info(f"Escalated '{name}' from {status} → {target}")
        return

    # Task is Done — check if interval has elapsed since completion
    done_date = last_touched(task)
    if not done_date or (today - done_date).days < int(recurrence_days):
        return

    # Reset the existing page for the next cycle
    name = prop_text(task, "Name")
    notion.pages.update(
        page_id=task["id"],
        properties={
            "Status": {"select": {"name": "P3"}},
            "period": {"rich_text": [{"text": {"content": today.isoformat()}}]},
        },
    )
    logger.info(f"Reset '{name}' for new cycle (automation={automation['id']})")


def handle_escalation_only(automation, today):
    existing = query_all(
        TASKS_DB_ID,
        {
            "and": [
                {"property": "automation_id", "rich_text": {"equals": automation["id"]}},
                {"property": "period", "rich_text": {"equals": "singleton"}},
            ]
        },
    )

    if existing:
        task = existing[0]
        if prop_select(task, "Status") == DONE_STATUS:
            # Auto-disable the automation
            notion.pages.update(
                page_id=automation["id"],
                properties={"active": {"checkbox": False}},
            )
            logger.info(f"Auto-disabled escalation_only automation {automation['id']} (task done)")
        else:
            maybe_escalate(task, automation, today)
    else:
        create_task(automation, "singleton", today)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


HANDLERS = {
    "monthly": handle_monthly,
    "after_completion": handle_after_completion,
    "escalation_only": handle_escalation_only,
}


def handler(event, context):
    today = date.today()
    automations = query_all(
        AUTOMATIONS_DB_ID,
        {"property": "active", "checkbox": {"equals": True}},
    )
    logger.info(f"Processing {len(automations)} active automations for {today}")

    for automation in automations:
        automation_name = prop_text(automation, "Name")
        recurrence_type = prop_select(automation, "recurrence_type")
        fn = HANDLERS.get(recurrence_type)
        if not fn:
            logger.warning(f"Unknown recurrence_type '{recurrence_type}' on '{automation_name}'")
            continue
        try:
            fn(automation, today)
        except Exception as e:
            logger.error(f"Error processing '{automation_name}': {e}", exc_info=True)
