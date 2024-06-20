import codewars_test as test
from kata import case_id

@test.describe("Sample tests")
def _():
    @test.it("should correctly identify kebab case")
    def __():
        test.assert_equals(case_id("hello-world"), "kebab")
        test.assert_equals(case_id("hello-to-the-world"), "kebab")

    @test.it("should correctly identify snake case")
    def __():
        test.assert_equals(case_id("hello_world"), "snake")
        test.assert_equals(case_id("hello_to_the_world"), "snake")

    @test.it("should correctly identify camel case")
    def __():
        test.assert_equals(case_id("helloWorld"), "camel")
        test.assert_equals(case_id("helloToTheWorld"), "camel")

    @test.it("should return 'none' for invalid cases")
    def __():
        test.assert_equals(case_id("hello-World"), "none")
        test.assert_equals(case_id("hello-To-The-World"), "none")
        test.assert_equals(case_id("good-Night"), "none")
        test.assert_equals(case_id("he--llo"), "none")