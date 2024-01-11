import codewars_test as test
from kata import fly_by

@test.describe("Example tests")
def test_group():
    @test.it("example tests")
    def test_case():
        test.assert_equals(fly_by('xxxxxx', '====T'), 'ooooox')
        test.assert_equals(fly_by('xxxxxxxxx', '==T'), 'oooxxxxxx')
        test.assert_equals(fly_by('xxxxxxxxxxxxxxx', '=========T'), 'ooooooooooxxxxx')
