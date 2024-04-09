from kata import who_took_the_car_key
import codewars_test as test

@test.describe('Basic Tests')
def basic_tests():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(who_took_the_car_key(
            ['01000001', '01101100', '01100101', '01111000', '01100001', '01101110',
             '01100100', '01100101', '01110010']
        ), 'Alexander')
        test.assert_equals(who_took_the_car_key(
            ['01001010', '01100101', '01110010', '01100101', '01101101', '01111001']
        ), 'Jeremy')
        test.assert_equals(who_took_the_car_key(
            ['01000011', '01101000', '01110010', '01101001', '01110011']
        ), 'Chris')
        test.assert_equals(who_took_the_car_key(
            ['01001010', '01100101', '01110011', '01110011', '01101001', '01100011',
             '01100001']
        ), 'Jessica')
        test.assert_equals(who_took_the_car_key(
            ['01001010', '01100101', '01110010', '01100101', '01101101', '01111001']
        ), 'Jeremy')
        