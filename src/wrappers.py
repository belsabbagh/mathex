from typing import Literal
from .types import Bracket, Expression, exp
from .symbols import bracket


def wrap(expression: Expression, start, end) -> str:
    """Wraps an expression with start and end."""
    expression = exp(expression)
    return start + expression + end


def wrap_begin_end(expression: Expression, mode: Literal["table", "matrix"]) -> str:
    """Wraps an expression with begin and end."""
    expression = exp(expression)
    return wrap(expression, f"\\begin{{{mode}}}", f"\\end{{{mode}}}")


def brackets(expression, b: tuple[Bracket, Bracket]) -> str:
    """Converts an expression to LaTeX form with brackets."""
    expression = exp(expression)
    l, r = map(bracket, b)
    return wrap(expression, f"\\left{l}", f"\\right{r}")
