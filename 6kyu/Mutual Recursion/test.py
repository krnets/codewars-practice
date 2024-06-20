import codewars_test as test
from kata import f, m

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(f(0),1)
        test.assert_equals(f(5),3)
        test.assert_equals(f(10),6)
        test.assert_equals(f(15),9)
        test.assert_equals(f(25),16)
        test.assert_equals(m(0),0)
        test.assert_equals(m(5),3)
        test.assert_equals(m(10),6)
        test.assert_equals(m(15),9)
        test.assert_equals(m(25),16)

    F,M= [],[]
    for i in range(0,10):
        F.append(f(i))
        M.append(m(i))

    @test.it("Sequence check I")
    def basic_test_cases():
        test.assert_equals(F,[1,1,2,2,3,3,4,5,5,6])
        test.assert_equals(M,[0,0,1,2,2,3,4,4,5,6])

    for i in range(10,25):
        F.append(f(i))
        M.append(m(i))

    @test.it("Sequence check II")
    def basic_test_cases():
        test.assert_equals(F,[1,1,2,2,3,3,4,5,5,6,6,7,8,8,9,9,10,11,11,12,13,13,14,14,15])
        test.assert_equals(M,[0,0,1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,14,14,15])