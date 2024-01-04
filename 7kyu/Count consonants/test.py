import codewars_test as test
from kata import consonant_count


@test.describe("Sample Tests")
def sample_tests():
    @test.it("works for some examples")
    def sample_tests():
        test.assert_equals(consonant_count(''), 0, 'Test string is empty string')
        test.assert_equals(consonant_count('aaaaa'), 0, 'Test string: "aaaaa"')
        test.assert_equals(consonant_count("XaeiouX"), 2, 'Test string: "XaeiouX"')
        test.assert_equals(consonant_count('Bbbbb'), 5, 'Test string: "Bbbbb"')
        test.assert_equals(consonant_count('helLo world'), 7, 'Test string: "helLo world"')
        test.assert_equals(consonant_count('h^$&^#$&^elLo world'), 7, 'Test string: "h^$&^#$&^elLo world"')
        test.assert_equals(consonant_count('0123456789'), 0, 'Test string: "0123456789"')
        test.assert_equals(consonant_count('012345_Cb'), 2, 'Test string: "012345_Cb"')
