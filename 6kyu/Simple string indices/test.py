import codewars_test as test
from kata import solve

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solve("((1)23(45))(aB)",0),10)
        test.assert_equals(solve("((1)23(45))(aB)",1),3)
        test.assert_equals(solve("((1)23(45))(aB)",2),-1)
        test.assert_equals(solve("((1)23(45))(aB)",6),9)
        test.assert_equals(solve("((1)23(45))(aB)",11),14)
        test.assert_equals(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",11),28)
        test.assert_equals(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",0),29)
        test.assert_equals(solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))",19),22)