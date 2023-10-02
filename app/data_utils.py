import json
import urllib.request


def get_chess_stats() -> dict:
    with urllib.request.urlopen(
        "https://api.chess.com/pub/player/thwardenheimer/stats"
    ) as url:
        data = json.load(url)

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
