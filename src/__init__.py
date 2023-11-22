from typing import Iterable
import src.symbols as syms
import src.wrappers as wrps
from src import types


def subscript(base: types.Expression, subscript: types.Expression) -> str:
    """Converts a subscript to LaTeX form."""
    base, subscript = types.params2expressions(base, subscript)
    return base + "_" + wrps.wrap(subscript, "{", "}")


def superscript(base: types.Expression, superscript: types.Expression) -> str:
    """Converts a superscript to LaTeX form."""
    base, subscript = types.params2expressions(base, subscript)
    return base + "^" + wrps.wrap(superscript, "{", "}")


def subscript_superscript(
    base: types.Expression, subscript: types.Expression, superscript: types.Expression
) -> str:
    """Converts a subscript and superscript to LaTeX form."""
    base, subscript, superscript = types.params2expressions(
        base, subscript, superscript
    )
    return superscript(subscript(base, subscript), superscript)


def arr2row(arr: Iterable) -> str:
    """Converts an array to LaTeX form."""
    return " & ".join(map(types.exp, arr))


def matrix(
    matrix: Iterable[Iterable], b: tuple[types.Bracket, types.Bracket] = None
) -> str:
    """Converts a matrix to LaTeX form."""
    matrix = wrps.wrap_begin_end(r"\\".join(map(arr2row, matrix)), "matrix")
    return wrps.brackets(matrix, (b[0], b[1])) if b is not None else matrix


def example_matrix(m: list[list], b: tuple[types.Bracket, types.Bracket] = None) -> str:
    """Creates a 4x4 matrix with dots to show the pattern."""
    cases = [0, syms.dots("c"), syms.dots("v"), syms.dots("d")]
    if len(m) != 4 or len(m[0]) != 4:
        raise ValueError("Matrix must be 4x4.")
    for i in range(4):
        for j in range(4):
            cases[0] = types.exp(m[i][j])
            cond_case = int(f"{int(i==2)}{int(j==2)}", 2)
            m[i][j] = cases[cond_case]
    return matrix(m, b)


def fraction(numerator: types.Expression, denominator: types.Expression) -> str:
    """Converts a fraction to LaTeX form."""
    numerator, denominator = types.params2expressions(numerator, denominator)
    return f"\\frac" + "".join(wrps.wrap(i, *r"{}") for i in [numerator, denominator])


def sum_latex(
    start: types.Expression, end: types.Expression, term: types.Expression
) -> str:
    """Converts a sum to LaTeX form."""
    start, end, term = types.params2expressions(start, end, term)
    return subscript_superscript("\\sum", start, end) + term


def product_latex(
    start: types.Expression, end: types.Expression, term: types.Expression
) -> str:
    """Converts a product to LaTeX form."""
    start, end, term = types.params2expressions(start, end, term)
    return subscript_superscript("\\prod", start, end) + term


def add_latex(*terms: types.Expression) -> str:
    """Formats terms into addition form."""
    terms = types.params2expressions(*terms)
    return " + ".join(terms)


def sub_latex(*terms: types.Expression) -> str:
    """Formats terms into subtraction form."""
    terms = types.params2expressions(*terms)
    return " - ".join(terms)


def mul_latex(
    *terms: types.Expression,
    operator: types.MulOperator = "",
) -> str:
    """Formats terms into multiplication form."""
    terms = types.params2expressions(*terms)
    op = syms.mulop(operator)
    op = f" {op} " if op != "" else op
    return op.join(terms)


def div_latex(*terms: types.Expression) -> str:
    terms = types.params2expressions(*terms)
    return " \\div ".join(terms)


def sqrt_latex(base: types.Expression) -> str:
    """Converts a square root to LaTeX form."""
    base = types.exp(base)
    return r"\sqrt{" + base + r"}"


def nth_root_latex(base: types.Expression, n: types.Expression) -> str:
    """Converts a nth root to LaTeX form."""
    base, n = types.params2expressions(base, n)
    if n == "2":
        return sqrt_latex(base)
    return r"\sqrt" + wrps.wrap(n, *"[]") + wrps.wrap(base, *r"{}")


def log_latex(base: types.Expression, exp: types.Expression) -> str:
    """Converts a logarithm to LaTeX form."""
    base, exp = types.params2expressions(base, exp)
    return subscript("\\log", base) + exp


def lim_latex(base: types.Expression, exp: types.Expression) -> str:
    """Converts a limit to LaTeX form."""
    base, exp = types.params2expressions(base, exp)
    return subscript("\\lim", base) + exp


def integral_latex(
    start: types.Expression, end: types.Expression, term: types.Expression
) -> str:
    """Converts an integral to LaTeX form."""
    start, end, term = types.params2expressions(start, end, term)
    return subscript_superscript("\\int", start, end) + term
