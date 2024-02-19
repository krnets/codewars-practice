import codewars_test as test
from kata import hex_hash

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hex_hash('kcxnjsklsHskjHDkl7878hHJk'), 218)
        test.assert_equals(hex_hash(''), 0)
        test.assert_equals(hex_hash('ThisIsATest!'), 120)
        test.assert_equals(hex_hash('dhsajkbfyewquilb4y83q903ybr8q9apf7\9ph79qw0-eq230br[wq87r0=18-[#20r370B 7Q0RFP23B79037902RF79WQ0[]]]'), 802)