import codewars_test as test
from kata import plane_seat

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(plane_seat('2B'), 'Front-Left')
        test.assert_equals(plane_seat('20B'), 'Front-Left')
        test.assert_equals(plane_seat('58I'), 'No Seat!!')
        test.assert_equals(plane_seat('60D'), 'Back-Middle')
        test.assert_equals(plane_seat('17K'), 'Front-Right')