import codewars_test as test
from kata import fusc
import random

@test.describe("The fusc function -- Part 1")
def all_tests():
    
    @test.it("Fixed Tests")
    def fixed_tests():
        results = [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3]
        
        for n in range(21):
            test.assert_equals(fusc(n), results[n], f"{n = }")
        test.assert_equals(fusc(85), 21, "n = 85")
        
        
    @test.it("Random Test Cases")
    def random_tests():

        def my_fusc(n):
            if n == 0: return 0
            if n == 1: return 1
            if n % 2 == 0: return my_fusc(n // 2)
            return my_fusc(n // 2) + my_fusc(n // 2 + 1)
    
        for _ in range(40):
            n = random.randrange(1, 201)
            expected = my_fusc(n)
            test.assert_equals(fusc(n), expected, f"{n = }")