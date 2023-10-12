from typing import Literal, Union

Bracket = Literal[
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "|",
    "\\|",
    "langle",
    "rangle",
    "lceil",
    "rceil",
    "lfloor",
    "rfloor",
]
MulOperator = Literal[".", "x", ""]


def __fmt_complex(c: complex) -> str:
    """Formats a complex number to LaTeX form."""
    if c.imag == 0:
        return str(c.real)
    if c.real == 0:
        return str(c.imag) + "i"
    if c.imag in [1, -1]:
        return str(c.real) + ("+" if c.imag == 1 else "-") + "i"
    return str(c).replace("(", "").replace(")", "").replace("j", "i")


MODES = {
    "str": lambda x: x,
    "int": lambda x: str(x),
    "float": lambda x: str(x),
    "complex": lambda x: __fmt_complex(x),
}
Expression = Union[str, int, float, complex]


def exp(expression: Expression) -> str:
    return MODES[type(expression).__name__](expression)


def params2expressions(*params: Expression) -> list[str]:
    return [exp(param) for param in params]
