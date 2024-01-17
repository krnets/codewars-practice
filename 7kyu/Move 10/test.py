import codewars_test as test
from kata import move_ten


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(move_ten("testcase"), "docdmkco")
        test.assert_equals(move_ten("codewars"), "mynogkbc")
        test.assert_equals(move_ten("exampletesthere"), "ohkwzvodocdrobo")
        test.assert_equals(move_ten("returnofthespacecamel"), "bodebxypdroczkmomkwov")
        test.assert_equals(move_ten("bringonthebootcamp"), "lbsxqyxdrolyydmkwz")
        test.assert_equals(move_ten("weneedanofficedog"), "goxoonkxyppsmonyq")
