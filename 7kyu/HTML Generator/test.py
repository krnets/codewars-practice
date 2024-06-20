import codewars_test as test
from kata import HTMLGen

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        htmlGen = HTMLGen()
        test.assert_equals(htmlGen.a('test'), '<a>test</a>')
        test.assert_equals(htmlGen.comment('test'), '<!--test-->')