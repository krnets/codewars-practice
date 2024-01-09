import codewars_test as test
from kata import remove_consecutive_duplicates

@test.describe("Tests")
def tests():

    def do_test(input, expected):
        actual = remove_consecutive_duplicates(input)
        test.assert_equals(actual, expected, f"for string: '{input}'\n")

    @test.it("Sample tests")
    def sample_tests():
        do_test("", "")
        do_test('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta', 'alpha beta gamma delta alpha beta gamma delta'),
        do_test("iIi IiI", "iIi IiI")
        do_test("aa a aa a aa", "aa a aa a aa")
        do_test("this his is is sih siht", "this his is sih siht")
        do_test("don't don t do not dont", "don't don t do not dont")