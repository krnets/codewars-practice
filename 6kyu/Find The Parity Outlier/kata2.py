import codewars_test as test

def find_outlier(integers):
    evens = [x for x in integers if x % 2 == 0]
    odds = [x for x in integers if x & 1]
    return evens[0] if len(evens) == 1 else odds[0]

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
        test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
    
    @test.it("More complex tests")
    def basic_test_cases():
        ints1 = [2,6,8,10,3]; # odd at the back
        ints2 = [2,6,8,200,700,1,84,10,4]; # odd in the middle
        ints3 = [17,6,8,10,6,12,24,36]; # odd in the front
        ints4 = [2,1,7,17,19,211,7]; # even in the front
        ints5 = [1,1,1,1,1,44,7,7,7,7,7,7,7,7]; # even in the middle
        ints6 = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,35,5,5,5,5,5,5,5,5,5,5,7,7,7,7,1000]; # even at the end
        ints7 = [2,-6,8,-10,-3]; # odd at the back, negative
        ints8 = [2,6,8,2,-66,34,-35,66,700,1002,-84,10,4]; # odd in the middle, negative
        ints9 = [-123456789,-18,6,-8,-10,6,12,-24,36]; # odd in the front, negative
        ints10 = [-20,1,7,17,19,211,7]; # even in the front, negative
        ints11= [1,1,-1,1,1,-44,7,7,7,7,7,7,7,7]; # even in the middle, negative
        ints12 = [1,0,0]; # odd answer, zeroes
        ints13 = [3,7,-99,81,90211,0,7]; # even in the middle, zero

        inputs = [ints1, ints2, ints3, ints4, ints5, ints6, ints7, ints8, ints9, ints10, ints11, ints12, ints13]
        expected = [3, 1, 17, 2, 44, 1000, -3, -35, -123456789, -20, -44, 1, 0]

        for i, (ins, e) in enumerate(zip(inputs, expected)):
            test.assert_equals(find_outlier(ins), e)