import codewars_test as test
from kata import arrays_similar

@test.describe('Example Tests')
def example_tests():    
    @test.it('Basic Test Cases')
    def basic_test_cases():
    
        arr1 = [1, 2, 2, 3, 4]
        arr2 = [2, 1, 2, 4, 3]
        arr3 = [1, 1, 2]
        arr4 = [4, 3, 2, 1, 1]
        arr5 = [1, 2, 2, 3]
        arr6 = [3, 3, 2, 1]
        arr7 = [1, 2]
        arr8 = ['1', 2]
        arr9 = ['1', 1]
        arr10 = [1, 1]
        arr11 = ['1', 1]
        arr12 = [1, '1']

        test.assert_equals(arrays_similar(arr1, arr2), True)
        test.assert_equals(arrays_similar(arr2, arr1), True)
        test.assert_equals(arrays_similar(arr11, arr12), True)

        test.assert_equals(arrays_similar(arr2, arr3), False)
        test.assert_equals(arrays_similar(arr3, arr4), False)
        test.assert_equals(arrays_similar(arr5, arr6), False)
        test.assert_equals(arrays_similar(arr7, arr8), False)
        test.assert_equals(arrays_similar(arr9, arr10), False)
