from src import mul_latex


def test_mul():
    assert mul_latex("x", "y") == "xy"
    assert mul_latex("x", "y", operator="x") == "x \\times y"
    assert mul_latex("x", "y", operator=".") == "x \\cdot y"
