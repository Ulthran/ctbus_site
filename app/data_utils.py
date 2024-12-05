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

#
# BEGIN SPOTIPY AUTHORIZATION-BASED CODE
#


def get_spotipy_auth_manager(
    session: SessionMixin, redirect_uri: str
) -> tuple[spotipy.cache_handler.FlaskSessionCacheHandler, spotipy.oauth2.SpotifyOAuth]:
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        scope="user-top-read playlist-read-private",
        cache_handler=cache_handler,
        show_dialog=True,
        redirect_uri=redirect_uri,
    )

    return cache_handler, auth_manager


def get_spotify_user(auth_manager: spotipy.oauth2.SpotifyOAuth) -> dict[str, str]:
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp.me()


NORMALIZED_AUDIO_FEATURES = [
    "danceability",
    "energy",
    "mode",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
]


def get_normalized_audio_features(
    auth_manager: spotipy.oauth2.SpotifyOAuth,
    time_frame: str = "medium_term",
    num_tracks: int = 20,
) -> dict[str, str]:
    sp = spotipy.Spotify(auth_manager=auth_manager)

    top_tracks = sp.current_user_top_tracks(
        limit=num_tracks, offset=0, time_range=time_frame
    )

    audio_features = sp.audio_features([track["id"] for track in top_tracks["items"]])

    ret = [
        {
            "x": NORMALIZED_AUDIO_FEATURES,
            "y": [track[key] for key in NORMALIZED_AUDIO_FEATURES],
            "name": [t["name"] for t in top_tracks["items"] if t["id"] == track["id"]][
                0
            ],
            "type": "bar",
        }
        for track in audio_features
    ]

    return ret


def get_playlists(auth_manager: spotipy.oauth2.SpotifyOAuth) -> list[str]:
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = sp.current_user_playlists()

    return [playlist["name"] for playlist in playlists["items"]]


def get_playlist(
    auth_manager: spotipy.oauth2.SpotifyOAuth, playlist_name: str
) -> dict[str, str]:
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = sp.current_user_playlists()

    playlist_id = None
    for playlist in playlists["items"]:
        if playlist["name"] == playlist_name:
            playlist_id = playlist["id"]
            break

    if not playlist_id:
        return {"error": "Playlist not found"}

    playlist = sp.playlist(playlist_id)

    playlist_features = sp.audio_features(
        [track["track"]["id"] for track in playlist["tracks"]["items"]]
    )

    # THIS SHOULD BE PASSED AS PARAMETER
    features = [
        "energy",
        "danceability",
        "acousticness",
        "instrumentalness",
        "valence",
        "liveness",
        "speechiness",
    ]

    return [
        {
            "x": [
                sum(
                    [
                        playlist["tracks"]["items"][j]["track"]["duration_ms"] / 60000
                        for j in range(0, i)
                    ]
                )
                for i in range(len(playlist["tracks"]["items"]))
            ],
            "y": [track[feature] for track in playlist_features],
            "text": [track["track"]["name"] for track in playlist["tracks"]["items"]],
            "textposition": "top",
            "name": feature,
            "type": "scatter",
        }
        for feature in features
    ]


def get_spotify_data(
    auth_manager: spotipy.oauth2.SpotifyOAuth,
    time_frame: str = None,
    num_tracks: int = None,
    playlistsQ: bool = False,
    playlist_name: str = None,
) -> Union[dict[str, str], list[str]]:
    if playlistsQ:
        print("playlistsQ")
        val = get_playlists(auth_manager)
        print(val)

        return get_playlists(auth_manager)
    elif time_frame and num_tracks:
        print("Normalized Audio Features")
        return get_normalized_audio_features(
            auth_manager, time_frame=time_frame, num_tracks=num_tracks
        )
    elif playlist_name:
        print("Playlist")
        return get_playlist(auth_manager, playlist_name)


#
# END SPOTIPY AUTHORIZATION-BASED CODE
#
