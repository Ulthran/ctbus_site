import json
import urllib.request
from typing import Dict


def get_chess_league_image() -> str:
    url = "https://api.chess.com/pub/player/thwardenheimer"

    if url.lower().startswith("http"):
        req = urllib.request.Request(url)
    else:
        raise ValueError from None

    # Hardcoded url doesn't need to be sanitized (and it is anyway)
    with urllib.request.urlopen(req) as resp:  # nosec
        data = json.load(resp)
        # The league string should be lower case
        league = str(data["league"]).lower()

        try:
            return (
                f"https://www.chess.com/bundles/web/images/leagues/badges/{league}.svg"
            )
        except KeyError:
            return "ERR"


def get_chess_stats() -> Dict[str, str]:
    url = "https://api.chess.com/pub/player/thwardenheimer/stats"

    if url.lower().startswith("http"):
        req = urllib.request.Request(url)
    else:
        raise ValueError from None

    # Hardcoded url doesn't need to be sanitized (and it is anyway)
    with urllib.request.urlopen(req) as resp:  # nosec
        data = json.load(resp)

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
