import codewars_test as test
from kata import zebulans_nightmare


@test.describe("Fixed tests")
def f():
    @test.it("")
    def check():
        test.assert_equals(zebulans_nightmare("camel_case"), "camelCase")
        test.assert_equals(zebulans_nightmare("zebulans_nightmare"), "zebulansNightmare")
        test.assert_equals(zebulans_nightmare("get_string"), "getString")
        test.assert_equals(zebulans_nightmare("convert_to_uppercase"), "convertToUppercase")
