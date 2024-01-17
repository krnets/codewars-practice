from kata import Dictionary
import codewars_test as test


@test.describe("Sample tests")
def basic_tests():
    d = Dictionary()

    @test.it("Testing for key 'Apple', should equal 'A fruit'")
    def _():
        d.newentry("Apple", "A fruit")
        test.assert_equals(d.look("Apple"), "A fruit")

    @test.it("Testing for key 'Soccer', should equal 'A sport'")
    def _():
        d.newentry("Soccer", "A sport")
        test.assert_equals(d.look("Soccer"), "A sport")

    @test.it("Testing for non-existing keys")
    def _():
        test.assert_equals(d.look("Hi"), "Can't find entry for Hi")
        test.assert_equals(d.look("Ball"), "Can't find entry for Ball")

    @test.it("Testing that entries are case sensitive")
    def _():
        test.assert_equals(d.look("soccer"), "Can't find entry for soccer")
        d.newentry("soccer", "a sport")
        test.assert_equals(d.look("soccer"), "a sport")
