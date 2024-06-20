import codewars_test as test
from kata import fibs_fizz_buzz

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = [
            (2, [1, 1]),
            (5, [1, 1, 2, 'Fizz', 'Buzz']),
            (7, [1, 1, 2, 'Fizz', 'Buzz', 8, 13]),
            (10, [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34, 'Buzz']),
            (15, [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34, 'Buzz', 89, 'Fizz', 233, 377, 'Buzz']),
            (20, [1,1,2,"Fizz","Buzz",8,13,"Fizz",34,"Buzz",89,"Fizz",233,377,"Buzz","Fizz",1597,2584,4181,"FizzBuzz"]),
            (1, [1]),
            (40, [1,1,2,"Fizz","Buzz",8,13,"Fizz",34,"Buzz",89,"Fizz",233,377,"Buzz","Fizz",1597,2584,4181,"FizzBuzz",10946,17711,28657,"Fizz","Buzz",121393,196418,"Fizz",514229,"Buzz",1346269,"Fizz",3524578,5702887,"Buzz","Fizz",24157817,39088169,63245986,"FizzBuzz"]),
        ]


        for args, expected in tests:
            test.assert_equals(fibs_fizz_buzz(args), expected)