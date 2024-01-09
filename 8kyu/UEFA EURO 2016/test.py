import codewars_test as test
from kata import uefa_euro_2016

@test.describe("Fixed tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]), "At match Germany - Ukraine, Germany won!");
        test.assert_equals(uefa_euro_2016(['Belgium', 'Italy'], [0, 2]), "At match Belgium - Italy, Italy won!")
        test.assert_equals(uefa_euro_2016(['Portugal', 'Iceland'], [1, 1]), "At match Portugal - Iceland, teams played draw.")
        test.assert_equals(uefa_euro_2016(['Albania', 'Switzerland'], [1, 2]), "At match Albania - Switzerland, Switzerland won!")
        test.assert_equals(uefa_euro_2016(['Republic of Ireland', 'Sweden'], [0, 0]), "At match Republic of Ireland - Sweden, teams played draw.")
