from src import matrix, example_matrix


def test_matrix():
    mat = [["x+y", 2], [3, 4]]
    assert matrix(mat).replace(" ", "") == r"\begin{matrix}x+y&2\\3&4\end{matrix}"


def test_matrix_brackets():
    mat = [["x+y", 2], [3, 4]]
    assert (
        matrix(mat, b=("(", ")")).replace(" ", "")
        == r"\left(\begin{matrix}x+y&2\\3&4\end{matrix}\right)"
    )


def test_example_matrix():
    mat = [
        ["n1", "n2", "n3", "n4"],
        ["n5", "n6", "n7", "n8"],
        ["n9", "n10", "n11", "n12"],
        ["n13", "n14", "n15", "n16"],
    ]
    assert (
        example_matrix(mat).replace(" ", "")
        == r"\begin{matrix}n1&n2&\cdots&n4\\n5&n6&\cdots&n8\\\vdots&\vdots&\ddots&\vdots\\n13&n14&\cdots&n16\end{matrix}"
    )
