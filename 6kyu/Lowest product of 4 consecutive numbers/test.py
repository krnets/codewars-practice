import codewars_test as test
from kata import lowest_product

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(lowest_product("123456789"),24);
        test.assert_equals(lowest_product("987654321"),24);
        test.assert_equals(lowest_product("234567899"),120); 

        test.assert_equals(lowest_product("2345611117899"),1);
        test.assert_equals(lowest_product("2305611117899"),0);
        test.assert_equals(lowest_product("9999998999999"),5832);

        test.assert_equals(lowest_product("333"),"Number is too small");
        test.assert_equals(lowest_product("3"),"Number is too small");
        test.assert_equals(lowest_product(""),"Number is too small");

        test.assert_equals(lowest_product("1234111532"),4,"Numbers should be consecutives");
        test.assert_equals(lowest_product("1234111321"),3,"Numbers should be consecutives");
        test.assert_equals(lowest_product("1324222251"),16,"Numbers should be consecutives");