import codewars_test as test
from kata import trim


@test.describe("trim")
def tests():
    @test.it("works for some examples")
    def _():
        test.assert_equals(trim("Creating kata is fun", 14), "Creating ka...")
        test.assert_equals(trim("He", 1), "H...")
        test.assert_equals(trim("Hey", 2), "He...")
        test.assert_equals(trim("Hey", 3), "Hey")
        test.assert_equals(trim("Coding rocks", 12), "Coding rocks")
        test.assert_equals(
            trim("Code Wars is pretty rad", 50), "Code Wars is pretty rad"
        )
        test.assert_equals(trim("London is freezing", 18), "London is freezing")
        test.assert_equals(trim("oddC FIzcs", 3), "odd...")
        test.assert_equals(trim("sr FS GMBoG JS", 1), "s...")
        test.assert_equals(trim("SWuO EwQo hZ urF Ewgre", 3), "SWu...")
