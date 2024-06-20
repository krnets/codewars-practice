import codewars_test as test
from kata import recycle

@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def it_1():
        a = [
            {"type": "rotten apples", "material": "organic"},
            {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
            {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
            {"type": "amazon box", "material": "paper"},
            {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
        ]
        b = (
            ["wine bottle", "amazon box", "beer bottle"],
            ["wine bottle", "beer bottle"],
            ["rotten apples", "out of date yogurt"],
            ["out of date yogurt"]
        )
        test.assert_equals(recycle(a), b)