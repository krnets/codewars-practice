import codewars_test as test
from kata import comfortable_word

@test.describe("Comfortable words")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(comfortable_word('yams'), True)
        test.assert_equals(comfortable_word('test'), False)