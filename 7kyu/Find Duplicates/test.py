import codewars_test as test
from kata import duplicates


@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']), [4, 3, 1])
        test.assert_equals(duplicates([0, 1, 2, 3, 4, 5]), [])
        test.assert_equals(duplicates(['1', 2, 4, '4', 3, '3', 1, 5, 3, 3, 3, 3]), [3])
        test.assert_equals(duplicates(['zut', 'alors', 1, 2, 4, 4, 3, 3, '1', 5, 3, 'zut']), [4, 3, 'zut'])
        test.assert_equals(duplicates([]), [])
        test.assert_equals(duplicates(['no', 'duplicates', 'here']), [])