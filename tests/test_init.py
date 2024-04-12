from src import init


def test_init() -> None:
    text = "test"
    assert init(text) == text
