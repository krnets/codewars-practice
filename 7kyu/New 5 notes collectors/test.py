import codewars_test as test
from kata import get_new_notes

@test.describe('Testing...')
def _():
    @test.it("Basic tests")
    def _():
        test.assert_equals(get_new_notes(2000, [500, 160, 400]),188)
        test.assert_equals(get_new_notes(1260, [500, 50, 100]),122)
        test.assert_equals(get_new_notes(3600, [1800, 350, 460, 500, 15]),95)
        test.assert_equals(get_new_notes(1995, [1500, 19, 44]),86)
        test.assert_equals(get_new_notes(10000, [1800, 500, 1200, 655, 150]),1139)
        test.assert_equals(get_new_notes(2300, [590, 1500, 45, 655, 150]),0)
        test.assert_equals(get_new_notes(5300, [1190, 1010, 1045, 55, 10, 19, 55]),383)
        test.assert_equals(get_new_notes(2000, [500, 495, 100, 900]),1)
        test.assert_equals(get_new_notes(2000, [500, 496, 100, 900]),0)
        test.assert_equals(get_new_notes(2000, [500, 494, 100, 900]),1)