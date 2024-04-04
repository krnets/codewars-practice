import codewars_test as test
from kata import expression_out


@test.describe("Basic tests")
def _():
    @test.it("")
    def _():
        test.assert_equals(expression_out("1 + 3"), "One Plus Three")
        test.assert_equals(expression_out("2 - 10"), "Two Minus Ten")
        test.assert_equals(expression_out("6 ** 9"), "Six To The Power Of Nine")
        test.assert_equals(expression_out("5 = 5"), "Five Equals Five")
        test.assert_equals(expression_out("7 * 4"), "Seven Times Four")
        test.assert_equals(expression_out("2 / 2"), "Two Divided By Two")
        test.assert_equals(expression_out("8 != 5"), "Eight Does Not Equal Five")
        test.assert_equals(expression_out("One & Eight"), "That's not an operator!")
        test.assert_equals(expression_out("One & Eight"), "That's not an operator!")
        test.assert_equals(expression_out("Four @ Five"), "That's not an operator!")
        test.assert_equals(expression_out("One $ Six"), "That's not an operator!")
        test.assert_equals(expression_out("Four One Six"), "That's not an operator!")
        test.assert_equals(expression_out("Seven One Six"), "That's not an operator!")
        test.assert_equals(expression_out("One ^ Eight"), "That's not an operator!")
