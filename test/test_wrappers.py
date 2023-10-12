from src import wrappers


def test_base_wrap():
    assert wrappers.wrap("x", *r"{}") == r"{x}"
