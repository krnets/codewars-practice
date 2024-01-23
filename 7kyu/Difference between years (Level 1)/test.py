import codewars_test as test
from kata import how_many_years

@test.describe('Basic Test')
def _():
    @test.it("Tests")
    def _():
        test.assert_equals(how_many_years ('1997/10/10', '2015/10/10'), 18);
        test.assert_equals(how_many_years ('1990/10/10', '2015/10/10'), 25);
        test.assert_equals(how_many_years ('2015/10/10', '1990/10/10'), 25);
        test.assert_equals(how_many_years ('1992/10/24', '2015/10/24'), 23);
        test.assert_equals(how_many_years ('2018/10/10', '2000/10/10'), 18);