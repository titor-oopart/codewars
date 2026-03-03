import codewars_test as test
from katas.kata09_5kyu_square_matrix_multiplication import matrix_mult


@test.describe("tests")
def _():
    @test.it("sample tests")
    def _():
        test.assert_equals(matrix_mult([[5]], [[6]]), [[30]])

        test.assert_equals(
            matrix_mult(
                [[1, 2], [3, 2]],
                #      x
                [[3, 2], [1, 1]],
            ),
            #      =
            [[5, 4], [11, 8]],
        )

        test.assert_equals(
            matrix_mult(
                [[9, 7], [0, 1]],
                #      x
                [[1, 1], [4, 12]],
            ),
            #      =
            [[37, 93], [4, 12]],
        )

        test.assert_equals(
            matrix_mult(
                [[1, 2, 3], [3, 2, 1], [2, 1, 3]],
                #       x
                [[4, 5, 6], [6, 5, 4], [4, 6, 5]],
            ),
            #        =
            [[28, 33, 29], [28, 31, 31], [26, 33, 31]],
        )
