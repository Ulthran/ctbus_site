import re
import requests
import spotipy

from flask.sessions import SessionMixin
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


def get_spotify_data(
    auth_manager: spotipy.oauth2.SpotifyOAuth,
    time_frame: str = "medium_term",
    num_tracks: int = 20,
) -> dict[str, str]:
    return get_normalized_audio_features(
        auth_manager, time_frame=time_frame, num_tracks=num_tracks
    )
