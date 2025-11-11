import codewars_test as test
from katas.kata05_6kyu_camel_case_method import camel_case


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(camel_case("test case"), "TestCase")
        test.assert_equals(camel_case("camel case method"), "CamelCaseMethod")
        test.assert_equals(camel_case("say hello "), "SayHello")
        test.assert_equals(camel_case(" camel case word"), "CamelCaseWord")
        test.assert_equals(camel_case(""), "")
