import codewars_test as test
from kata import fix


# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(fix(""), "")
        test.assert_equals(fix("hi."), "Hi.")
        test.assert_equals(
            fix(
                "hello. my name is inigo montoya. you killed my father. prepare to die."
            ),
            "Hello. My name is inigo montoya. You killed my father. Prepare to die.",
        )
