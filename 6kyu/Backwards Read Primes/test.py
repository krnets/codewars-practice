import codewars_test as test
from kata import backwards_prime

@test.describe('Tests')
     
def fixed_tests():
    def testing(n, m, exp):
        # so already passed solutions with camelCase name are not invalidated
        actual = backwards_prime(n, m)
        test.assert_equals(actual, exp)
        
    @test.it('Basic Tests')
    def basic_tests1():
        a1 = [13, 17, 31, 37, 71, 73, 79, 97]
        testing(1, 97, a1)  
        a1 = [7027, 7043, 7057]
        testing(7000, 7100, a1)  
        a8 = []
        testing(400, 503, a8)
        