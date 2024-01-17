import codewars_test as test
from kata import hello_world


@test.describe("Tests")
def full():
    @test.it("Should work")
    def _():
        test.assert_equals(hello_world(), "Hello, World!")
