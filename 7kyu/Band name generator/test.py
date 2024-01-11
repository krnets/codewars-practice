import codewars_test as test
from kata import band_name_generator

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(band_name_generator("knife"), "The Knife")
        test.assert_equals(band_name_generator("tart"), "Tartart")
        test.assert_equals(band_name_generator("sandles"), "Sandlesandles")
        test.assert_equals(band_name_generator("bed"), "The Bed")
        test.assert_equals(band_name_generator("qq"), "Qqq")
        