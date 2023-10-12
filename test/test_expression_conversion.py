from src.types import exp


def test_int():
    assert exp(1) == "1"


def test_float():
    assert exp(1.0) == "1.0"


def test_complex():
    assert exp(1 + 1j) == "1+1i"


def test_str():
    assert exp("1") == "1"
