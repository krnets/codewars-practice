from kata import solve
import codewars_test as test


@test.it("Basic tests")
def basic_test_cases():
    test.assert_equals(solve("bgA5<1d-tOwUZTS8yQ"), [7, 6, 3, 2])
    test.assert_equals(solve("Codewars@codewars123.com"), [1, 18, 3, 2])
    test.assert_equals(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"), [9, 9, 6, 9])
    test.assert_equals(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"), [15, 8, 6, 9])
    test.assert_equals(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10, 7, 3, 6])
    test.assert_equals(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7, 13, 4, 10])
