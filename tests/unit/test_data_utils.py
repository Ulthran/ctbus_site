from app.data_utils import get_chess_stats


def test_get_chess_stats():
    # Chess.com's "unofficial" API, meaning they recognize people use it as is
    # but don't provide guarantees that it will stay the same
    # I guess that makes this not really a unit test. Oh well :/
    assert not any([v == "ERR" for k, v in get_chess_stats().items()])
