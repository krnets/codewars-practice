from kata import name_in_str
import codewars_test as test

@test.describe("Basic tests")
def basic_tests():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(name_in_str("Across the rivers", "chris"), True)
        test.assert_equals(name_in_str("Next to a lake", "chris"), False)
        test.assert_equals(name_in_str("Under a sea", "chris"), False)
        test.assert_equals(name_in_str("A crew that boards the ship", "chris"), False)
        test.assert_equals(name_in_str("A live son", "Allison"), False)
        test.assert_equals(name_in_str("Just enough nice friends","Jennifer"),False)
        test.assert_equals(name_in_str("thomas","Thomas"),True)
        test.assert_equals(name_in_str("pippippi","Pippi"),True)
        test.assert_equals(name_in_str("pipipp","Pippi"),False)
        test.assert_equals(name_in_str("ppipip","Pippi"),False)