import codewars_test as test
from katas.kata08_5kyu_simple_pig_latin import pig_it


@test.describe("Simple Pig Latin")
def tests():
    test.assert_equals(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
    test.assert_equals(pig_it("This is my string"), "hisTay siay ymay tringsay")
