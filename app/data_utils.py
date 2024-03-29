import re
import requests
from . import PCMP_REPOS


def get_chess_stats() -> dict[str, str]:
    url = "https://api.chess.com/pub/player/thwardenheimer/stats"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }

    reponse = requests.get(url, headers=headers, timeout=5)
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


def pcmp_repo_badges(repos: list[str] = PCMP_REPOS) -> dict[str, list[str]]:
    d = {repo: [] for repo in repos}

    for repo in repos:
        try:
            text = requests.get(
                f"https://raw.githubusercontent.com/{repo}/main/README.md", timeout=5
            ).text
        except requests.exceptions.RequestException:
            continue
        if text.startswith("404: Not Found"):
            try:
                text = requests.get(
                    f"https://raw.githubusercontent.com/{repo}/master/README.md",
                    timeout=5,
                ).text
            except requests.exceptions.RequestException:
                continue

        # Use regex to find badge URLs
        badge_urls = re.findall(r"\[!\[.*\]\((.*?)\)\]\(.*\)", text)
        print(badge_urls)
        d[repo] = badge_urls

    return d
