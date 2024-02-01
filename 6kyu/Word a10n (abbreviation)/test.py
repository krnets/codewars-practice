import codewars_test as test
from kata import abbreviate


@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(abbreviate("internationalization"), "i18n")
        test.assert_equals(abbreviate("accessibility"), "a11y")
        test.assert_equals(abbreviate("Accessibility"), "A11y")
        test.assert_equals(abbreviate("elephant-ride"), "e6t-r2e")
        test.assert_equals(abbreviate("elephant-rides are really fun!"), "e6t-r3s are r4y fun!")

# abbreviate("elephant-rides are really fun!")
#             ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
#  words (^):   "elephant" "rides" "are" "really" "fun"
#                 123456     123     1     1234     1
#  ignore short words:               X              X

#  abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
#  all non-word characters (*) remain in place
#                      "-"      " "    " "     " "     "!"
# === "e6t-r3s are r4y fun!"
