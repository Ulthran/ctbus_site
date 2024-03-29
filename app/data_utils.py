import asyncio
import re
import requests
from . import PCMP_REPOS


def get_chess_stats() -> dict[str, str]:
    url = "https://api.chess.com/pub/player/thwardenheimer/stats"

    reponse = requests.get(url)
    data = reponse.json()

    ret_dict = {}

    try:
        ret_dict["tactics_highest_rating"] = data["tactics"]["highest"]["rating"]
    except KeyError:
        ret_dict["tactics_highest_rating"] = "ERR"

    try:
        ret_dict["bullet_last_rating"] = data["chess_bullet"]["last"]["rating"]
    except KeyError:
        ret_dict["bullet_last_rating"] = "ERR"

    try:
        ret_dict["blitz_last_rating"] = data["chess_blitz"]["last"]["rating"]
    except KeyError:
        ret_dict["blitz_last_rating"] = "ERR"

    try:
        ret_dict["rapid_last_rating"] = data["chess_rapid"]["last"]["rating"]
    except KeyError:
        ret_dict["rapid_last_rating"] = "ERR"

    try:
        ret_dict["daily_last_rating"] = data["chess_daily"]["last"]["rating"]
    except KeyError:
        ret_dict["daily_last_rating"] = "ERR"

    return ret_dict


async def aiter(iterable: list[str]):
    for i in iterable:
        yield i


async def get_repo_badges_async() -> dict[str, list[str]]:
    d = {repo: [] for repo in PCMP_REPOS}

    async for repo in aiter(PCMP_REPOS):
        response = requests.get(
            f"https://api.github.com/repos/{repo}/actions/workflows"
        )

        try:
            d[repo] = [
                workflow["badge_url"] for workflow in response.json()["workflows"]
            ]
        except KeyError:
            pass

    return d


def pcmp_repo_badges1() -> dict[str, list[str]]:
    # Ideally we would use the GraphQL endpoint for batching these but it seems like currently there is no link between repos and workflows https://github.com/orgs/community/discussions/56300
    return asyncio.run(get_repo_badges_async())


def pcmp_repo_badges() -> dict[str, list[str]]:
    d = {repo: [] for repo in PCMP_REPOS}

    for repo in PCMP_REPOS:
        try:
            text = requests.get(
                f"https://raw.githubusercontent.com/{repo}/main/README.md"
            ).text
        except requests.exceptions.RequestException:
            continue
        if text.startswith("404: Not Found"):
            try:
                text = requests.get(
                    f"https://raw.githubusercontent.com/{repo}/master/README.md"
                ).text
            except requests.exceptions.RequestException:
                continue

        # Use regex to find badge URLs
        badge_urls = re.findall(r"\[!\[.*\]\((.*?)\)\]\(.*\)", text)
        print(badge_urls)
        d[repo] = badge_urls

    return d
