import codewars_test as test
from kata import title_case

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(title_case(''), '')
        test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
        test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
        test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')