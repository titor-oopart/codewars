import codewars_test as test
from katas.kata01_5kyu_calculating_with_functions import (
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    zero,
    times,
    divided_by,
    minus,
    plus,
)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(seven(times(five())), 35)
        test.assert_equals(four(plus(nine())), 13)
        test.assert_equals(eight(minus(three())), 5)
        test.assert_equals(six(divided_by(two())), 3)
