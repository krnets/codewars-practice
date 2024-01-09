import codewars_test as test
from kata import switcher

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(switcher(['24', '12', '23', '22', '4', '26', '9', '8']), 'codewars')
        test.assert_equals(switcher(['25','7','8','4','14','23','8','25','23','29','16','16','4']), 'btswmdsbd kkw')
        test.assert_equals(switcher(['4', '24']), 'wc')
        test.assert_equals(switcher(['12']), 'o')
        test.assert_equals(switcher(['12','28','25','21','25','7','11','22','15']), 'o?bfbtpel' )