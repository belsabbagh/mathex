from typing import Literal
from .types import Bracket, MulOperator

NoEscapeBrackets = [
    "{",
    "}",
    "langle",
    "rangle",
    "lceil",
    "rceil",
    "lfloor",
    "rfloor",
]


def bracket(b: Bracket):
    return "\\" + b if b in NoEscapeBrackets else b


def mulop(op: MulOperator) -> str:
    if op not in [".", "x", ""]:
        raise ValueError("op must be either '.', 'x', or nothing")
    ops = {"x": "\\times", ".": "\\cdot"}
    return ops.get(op, op)


def dots(mode: Literal["l", "c", "v", "d"]) -> str:
    """Returns the appropriate dots for the mode."""
    if mode not in "lcvd":
        raise ValueError("mode must be either 'l', 'c', 'v', or 'd'")
    return f"\\{mode}dots"
