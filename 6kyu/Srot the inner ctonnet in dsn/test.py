import codewars_test as test
from kata import sort_the_inner_content


@test.describe("kata tests")
def tests():
    @test.it("example tests")
    def tests():
        test.assert_equals(sort_the_inner_content("sort the inner content in descending order"), "srot the inner ctonnet in dsnnieedcg oredr");
        test.assert_equals(sort_the_inner_content("wait for me"), "wiat for me");
        test.assert_equals(sort_the_inner_content("this kata is easy"), "tihs ktaa is esay");