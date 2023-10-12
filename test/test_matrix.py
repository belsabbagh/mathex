from src import matrix


def test_matrix():
    mat = [["x+y", 2], [3, 4]]
    assert matrix(mat).replace(" ", "") == r"\begin{matrix}x+y&2\\3&4\end{matrix}"


def test_matrix_brackets():
    mat = [["x+y", 2], [3, 4]]
    assert (
        matrix(mat, b=("(", ")")).replace(" ", "")
        == r"\left(\begin{matrix}x+y&2\\3&4\end{matrix}\right)"
    )