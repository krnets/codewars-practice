from kata import is_prime
import codewars_test as test

@test.describe("Check for prime numbers")
def basic_tests():
    @test.it('Fixed tests')
    def it1():
        test.assert_equals(is_prime(0),False)
        test.assert_equals(is_prime(1),False)
        test.assert_equals(is_prime(2),True)
        test.assert_equals(is_prime(3),True)
        test.assert_equals(is_prime(11),True)
        test.assert_equals(is_prime(12),False)
        test.assert_equals(is_prime(61),True)
        test.assert_equals(is_prime(571),True)
        test.assert_equals(is_prime(573),False)
        test.assert_equals(is_prime(25),False)
    
@test.describe("Random Tests")
def random_tests():
    
    from random import randint
    
    def sol(n):
        return n == 2 or n % 2 and n > 2 and all(n % i for i in range(3, int(n ** .5) + 1, 2))
    
    for _ in range(100):
        
        num = randint(0, 10000)
        @test.it(f"Testing for is_prime({num})")
        def test_case():
            test.assert_equals(is_prime(num), sol(num), "It should work for random inputs too")