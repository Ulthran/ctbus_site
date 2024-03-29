from app.data_utils import get_chess_stats, pcmp_repo_badges


def test_get_chess_stats():
    # Chess.com's "unofficial" API, meaning they recognize people use it as is
    # but don't provide guarantees that it will stay the same
    assert not any([v == "ERR" for k, v in get_chess_stats().items()])


def test_pcmp_repo_badges():
    assert pcmp_repo_badges(["Ulthran/ctbus_site"]) == {
        "Ulthran/ctbus_site": [
            "https://github.com/Ulthran/ctbus_site/actions/workflows/main.yml/badge.svg",
            "https://img.shields.io/badge/renovate-enabled-brightgreen.svg",
            "https://app.codacy.com/project/badge/Grade/07edb64af1c544439190dff82571e7a5",
            "https://snyk.io/test/github/Ulthran/ctbus_site/badge.svg",
        ]
    }
