import codewars_test as test
from kata import string_expansion


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Normal cases")
    def _():
        test.assert_equals(string_expansion('3D2a5d2f'), 'DDDaadddddff')
        test.assert_equals(string_expansion('4D1a8d4j3k'), 'DDDDaddddddddjjjjkkk')
        test.assert_equals(string_expansion('4D2a8d4j2f'), 'DDDDaaddddddddjjjjff')
        test.assert_equals(string_expansion('3n6s7f3n'), 'nnnssssssfffffffnnn')
        test.assert_equals(string_expansion('0d4n8d2b'), 'nnnnddddddddbb')
        test.assert_equals(string_expansion('0c3b1n7m'), 'bbbnmmmmmmm')
        test.assert_equals(string_expansion('7m3j4ik2a'), 'mmmmmmmjjjiiiikkkkaa')
        test.assert_equals(string_expansion('3A5m3B3Y'), 'AAAmmmmmBBBYYY')
        test.assert_equals(string_expansion('5M0L8P1'), 'MMMMMPPPPPPPP')
        test.assert_equals(string_expansion('2B'), 'BB')
        test.assert_equals(string_expansion('7M1n3K'), 'MMMMMMMnKKK')
        test.assert_equals(string_expansion('A4g1b4d'), 'Aggggbdddd')

    @test.it("Repeated numerals")
    def _():
        test.assert_equals(string_expansion('111111'), '')
        test.assert_equals(string_expansion('4d324n2'), 'ddddnnnn')
        test.assert_equals(string_expansion('5919nf3u'), 'nnnnnnnnnfffffffffuuu')
        test.assert_equals(string_expansion('2n1k523n4i'), 'nnknnniiii')
        test.assert_equals(string_expansion('6o23M32d'), 'ooooooMMMdd')
        test.assert_equals(string_expansion('1B44n3r'), 'Bnnnnrrr')
        test.assert_equals(string_expansion('M21d1r32'), 'Mdr')
        test.assert_equals(string_expansion('23M31r2r2'), 'MMMrrr')
        test.assert_equals(string_expansion('8494mM25K2A'), 'mmmmMMMMKKKKKAA')
        test.assert_equals(string_expansion('4A46D6B3C'), 'AAAADDDDDDBBBBBBCCC')
        test.assert_equals(string_expansion('23D42B3A'), 'DDDBBAAA')
        test.assert_equals(string_expansion('143D36C1A'), 'DDDCCCCCCA')

    @test.it("Repeated alphabetic characters")
    def _():
        test.assert_equals(string_expansion('asdf'), 'asdf')
        test.assert_equals(string_expansion('23jbjl1eb'), 'jjjbbbjjjllleb')
        test.assert_equals(string_expansion('43ibadsr3'), 'iiibbbaaadddsssrrr')
        test.assert_equals(string_expansion('123p9cdbjs'), 'pppcccccccccdddddddddbbbbbbbbbjjjjjjjjjsssssssss')
        test.assert_equals(string_expansion('2309ew7eh'), 'eeeeeeeeewwwwwwwwweeeeeeehhhhhhh')
        test.assert_equals(string_expansion('312987rfebd'), 'rrrrrrrfffffffeeeeeeebbbbbbbddddddd')
        test.assert_equals(string_expansion('126cgec'), 'ccccccggggggeeeeeecccccc')
        test.assert_equals(string_expansion('1chwq3rfb'), 'chwqrrrfffbbb')
        test.assert_equals(string_expansion('389fg21c'), 'fffffffffgggggggggc')
        test.assert_equals(string_expansion('239vbsac'), 'vvvvvvvvvbbbbbbbbbsssssssssaaaaaaaaaccccccccc')
        test.assert_equals(string_expansion('davhb327vuc'), 'davhbvvvvvvvuuuuuuuccccccc')
        test.assert_equals(string_expansion('cvyb239bved2dv'), 'cvybbbbbbbbbbvvvvvvvvveeeeeeeeedddddddddddvv')

    @test.it("Empty string")
    def _():
        test.assert_equals(string_expansion(''), '')