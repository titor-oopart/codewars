import codewars_test as test
from katas.kata10_first_non_repeating_character import first_non_repeating_letter


@test.describe("Sample Tests")
def basic_tests():
    @test.it("Should handle simple cases")
    def _():
        test.assert_equals(first_non_repeating_letter("a"), "a")
        test.assert_equals(first_non_repeating_letter("stress"), "t")
        test.assert_equals(first_non_repeating_letter("moonmen"), "e")

    @test.it("Should handle empty strings")
    def _():
        test.assert_equals(first_non_repeating_letter(""), "")

    @test.it("Should handle strings without unique characters")
    def _():
        test.assert_equals(first_non_repeating_letter("abba"), "")
        test.assert_equals(first_non_repeating_letter("aa"), "")

    @test.it("Should handle exotic characters")
    def _():
        test.assert_equals(first_non_repeating_letter("~><#~><"), "#")
        test.assert_equals(first_non_repeating_letter("hello world, eh?"), "w")

    @test.it("Should handle letter case correctly")
    def _():
        test.assert_equals(first_non_repeating_letter("sTreSS"), "T")
        test.assert_equals(
            first_non_repeating_letter("Go hang a salami, I'm a lasagna hog!"), ","
        )
        test.assert_equals(
            first_non_repeating_letter("Who is my widdle silly mopy doggy then?"), "p"
        )
