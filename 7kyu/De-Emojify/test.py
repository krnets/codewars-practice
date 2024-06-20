from kata import deemojify
import codewars_test as test


@test.describe("Your de-emojify function")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("should properly de-emojify fixed strings")
    def test_second_oldest_first():
        test.assert_equals(deemojify(":D :) :/  :D :) :|"), "hi")
        test.assert_equals(
            deemojify(
                ";) >(  :D :) :D  :D :) ^.^  :D :) ^.^  :D :D :D  >:C >(  :D :D :(  :D :D :D  :D :D :/  :D :) ^.^  :D :) :)  >:C >:C"
            ),
            "Hello world!",
        )
        test.assert_equals(deemojify(":)"), "\x00")
