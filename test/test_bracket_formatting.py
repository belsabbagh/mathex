from src.symbols import bracket


def test_fmt():
    b = bracket("(")
    assert b == r"("


def test_escape_fmt():
    b = bracket("{")
    assert b == r"\{"
