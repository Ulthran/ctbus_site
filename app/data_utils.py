import re
import requests
import spotipy
from flask.sessions import SessionMixin
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Union
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


#
# BEGIN SPOTIPY CREDENTIAL-BASED CODE
#


def get_ctbus_monthly_playlists() -> list[dict[str, str]]:
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = sp.user_playlists("charlie_bushman")
    monthlies = []
    while playlists:
        # Note that apparently some playlists' apostrophe is encoded as ' while others are ‘ so we search both with ['‘]
        playlists["items"] = [p for p in playlists["items"] if p]
        playlists["items"] = [
            p
            for p in playlists["items"]
            if re.search(r"[A-Z][a-z]{2} ['‘]\d{2}", p["name"])
        ]
        for playlist in playlists["items"]:
            playlist["name"] = playlist["name"].replace("‘", "'")
            monthlies.append(playlist)
        if playlists["next"]:
            playlists = sp.next(playlists)
        else:
            playlists = None

    # Sort monthlies by name first sorting by the year (last two digits) and then month (first three characters)
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    monthlies.sort(
        key=lambda x: (int(x["name"][-2:]), months.index(x["name"][:3])), reverse=True
    )

    # Verify that all the fields used on the page template exist for each entry
    for playlist in monthlies:
        try:
            playlist["external_urls"]["spotify"]
        except KeyError:
            print(f"Playlist {playlist['name']} has no Spotify URL: {playlist}")
            playlist["external_urls"] = {"spotify": "#"}
        try:
            playlist["images"][2]["url"]
        except KeyError:
            print(f"Playlist {playlist['name']} has no images: {playlist}")
            playlist["images"] = [{}, {}, {"url": "#"}]
        except IndexError:
            print(f"Playlist {playlist['name']} has no 2nd image: {playlist}")
            playlist["images"] = [{}, {}, {"url": "#"}]

    return monthlies


#
# END SPOTIPY CREDENTIAL-BASED CODE
#
