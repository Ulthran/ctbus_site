import json
import spotipy
import urllib.request

from flask.sessions import SessionMixin
from typing import Dict, Tuple


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


def get_spotipy_auth_manager(
    session: SessionMixin, redirect_uri: str
) -> Tuple[spotipy.cache_handler.FlaskSessionCacheHandler, spotipy.oauth2.SpotifyOAuth]:
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        scope="user-top-read",
        cache_handler=cache_handler,
        show_dialog=True,
        redirect_uri=redirect_uri,
    )

    return cache_handler, auth_manager


def get_spotify_user(auth_manager: spotipy.oauth2.SpotifyOAuth) -> Dict[str, str]:
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
) -> Dict[str, str]:
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
) -> Dict[str, str]:
    return get_normalized_audio_features(
        auth_manager, time_frame=time_frame, num_tracks=num_tracks
    )
