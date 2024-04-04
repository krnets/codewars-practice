import codewars_test as test
from kata import substring_test

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(substring_test("Something","Home"), True)
        test.assert_equals(substring_test("Something","Fun"), False)
        test.assert_equals(substring_test("Something",""), False)
        test.assert_equals(substring_test("","Something"), False)
        test.assert_equals(substring_test("BANANA","banana"), True)
        test.assert_equals(substring_test("test","lllt"), False)
        test.assert_equals(substring_test("",""), False)
        test.assert_equals(substring_test("1234567","541265"), True)
        test.assert_equals(substring_test("supercalifragilisticexpialidocious","SoundOfItIsAtrocious"), True)
        test.assert_equals(substring_test("LoremipsumdolorsitametconsecteturadipiscingelitAeneannonal"
                                          "iquetligulautplaceratorciSuspendissepotentiMorbivolutpatau"
                                          "ctoripsumegetaliquamPhasellusidmagnaelitNullamerostelluste"
                                          "mporquismolestieaornarevitaediamNullaaliquamrisusnonviverr"
                                          "asagittisInlaoreetultricespretiumVestibulumegetnullatincid"
                                          "untsempersemacrutrumfelisPraesentpurusarcutempusnecvariusi"
                                          "dultricesaduiPellentesqueultriciesjustolobortisrhoncusdign"
                                          "issimNuncviverraconsequatblanditUtbibendumatlacusactristiq"
                                          "ueAliquamimperdietnuncsempertortorefficiturviverra","thisisalongstringtest"), True)