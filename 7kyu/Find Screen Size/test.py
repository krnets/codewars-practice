import codewars_test as test
from kata import find_screen_height


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(find_screen_height(1024, "4:3"), "1024x768")
        test.assert_equals(find_screen_height(1280, "16:9"), "1280x720")
        test.assert_equals(find_screen_height(3840, "32:9"), "3840x1080")
        test.assert_equals(find_screen_height(1600, "4:3"), "1600x1200")
        test.assert_equals(find_screen_height(1280, "5:4"), "1280x1024")
        test.assert_equals(find_screen_height(2160, "3:2"), "2160x1440")
        test.assert_equals(find_screen_height(1920, "16:9"), "1920x1080")
        test.assert_equals(find_screen_height(5120, "32:9"), "5120x1440")
