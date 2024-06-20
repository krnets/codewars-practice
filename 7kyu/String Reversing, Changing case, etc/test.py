import codewars_test as test
from kata import reverse_and_mirror


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(reverse_and_mirror("FizZ", "buZZ"), "zzUB@@@zZIffIZz")
        test.assert_equals(
            reverse_and_mirror("String Reversing", "Changing Case"),
            "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING",
        )
        s1, s2 = "String Reversing", "Changing Case"
        test.assert_equals(
            reverse_and_mirror(s1, s2),
            "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING",
        )

        s1, s2 = "FizZ", "buZZ"
        test.assert_equals(reverse_and_mirror(s1, s2), "zzUB@@@zZIffIZz")

        s1, s2 = "way to inVert", "caSe of string"
        test.assert_equals(
            reverse_and_mirror(s1, s2), "GNIRTS FO EsAC@@@TREvNI OT YAWWAY TO INvERT"
        )

        s1, s2 = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
            "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate",
        )
        test.assert_equals(
            reverse_and_mirror(s1, s2),
            "ETATPULOV AE NI IUQ TIREDNEHERPER ERUI MUE LEV METUA SIUq ?RUTAUQESNOC IDOMMOC AE XE DIUQILA TU ISIN ,MASOIROBAL TIPICSUS SIROPROC MALLU MENOITATICREXE MURTSON SIUQ ,MAINEV AMINIM DA MINE Tu@@@AUQILA ANGAM EROLOD TE EROBAL TU TNUDIDICNI ROPMET DOMSUIE OD DES ,TILE GNICSIPIDA RUTETCESNOC ,TEMA TIS ROLOD MUSPI MEROllOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA",
        )
