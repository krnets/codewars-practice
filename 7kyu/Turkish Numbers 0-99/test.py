from kata import get_turkish_number
import codewars_test as test


@test.describe("Turkish numbers")
def turkish_numbers():
    @test.it("Example tests")
    def example_tests():
        test.assert_equals(get_turkish_number(1), "bir")
        test.assert_equals(get_turkish_number(10), "on")
        test.assert_equals(get_turkish_number(60), "altmış")
        test.assert_equals(get_turkish_number(13), "on üç")
        test.assert_equals(get_turkish_number(27), "yirmi yedi")
        test.assert_equals(get_turkish_number(38), "otuz sekiz")
        test.assert_equals(get_turkish_number(77), "yetmiş yedi")
        test.assert_equals(get_turkish_number(94), "doksan dört")
