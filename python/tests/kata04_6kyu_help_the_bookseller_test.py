import codewars_test as test
from katas.kata04_6kyu_help_the_bookseller import stock_list


@test.describe("Testing")
def _():
    @test.it("Tests")
    def _():
        # example from description
        b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
        c = ["A", "B", "C", "W"]
        test.assert_equals(
            stock_list(b, c), "(A : 20) - (B : 114) - (C : 50) - (W : 0)"
        )

        b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B", "C", "D"]
        test.assert_equals(
            stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"
        )

        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")
