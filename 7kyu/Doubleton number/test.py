import codewars_test as test
from kata import doubleton

@test.describe("Fixed Tests")
def test_group():
    @test.it("Fixed Tests Cases")
    def test_case():
        test.assert_equals(doubleton(120), 121, 'Wrong result for 120. It should be 121')
        test.assert_equals(doubleton(1234), 1311, 'Wrong result for 1234. It should be 1311')
        test.assert_equals(doubleton(10), 12, 'Wrong result for 10. It should be 12')
        test.assert_equals(doubleton(1), 10, 'Wrong result for 1. It should be 10')
        test.assert_equals(doubleton(111), 112, 'Wrong result for 111. It should be 112')