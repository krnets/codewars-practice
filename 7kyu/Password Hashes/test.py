from kata import pass_hash
import codewars_test as test


@test.describe("Basic tests")
def basic_tests():
    @test.it("Simple text")
    def it1():
        test.assert_equals(pass_hash("password"), "5f4dcc3b5aa765d61d8327deb882cf99")
        test.assert_equals(pass_hash("abc123"), "e99a18c428cb38d5f260853678922e03")
