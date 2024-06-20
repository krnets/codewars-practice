import codewars_test as test
from kata import negation_value

@test.describe("Fixed tests")
def fixed_tests():
    test.assert_equals(negation_value("!", False), True)
    test.assert_equals(negation_value("!", True), False)
    test.assert_equals(negation_value("!!!", []), True)
    test.assert_equals(negation_value('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', []), False)
    test.assert_equals(negation_value('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', []), True)
    test.assert_equals(negation_value('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', None), False)