import codewars_test as test
from kata import run_length_encoding

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(run_length_encoding(''), [])
        test.assert_equals(run_length_encoding("abc"), [[1,'a'], [1,'b'], [1,'c']])
        test.assert_equals(run_length_encoding("aab"), [[2,'a'], [1,'b']])
        test.assert_equals(run_length_encoding("hello world!"), [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']])
        test.assert_equals(run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb"), [[34,'a'], [3,'b']])
        test.assert_equals(run_length_encoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"), [[12,'W'], [1,'B'], [12,'W'], [3,'B'], [24,'W'], [1,'B'], [14,'W']])
