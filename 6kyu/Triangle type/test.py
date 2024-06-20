from kata import triangle_type
import codewars_test as test

def do_test(sides, expected):
    type = ["INVALID", "ACUTE", "RIGHT", "OBTUSE"][expected]
    msg = "Sides = ({}, {}, {}), type = {}".format(*sides, type)
    actual = triangle_type(sides[0], sides[1], sides[2])
    test.assert_equals(actual, expected, msg)

@test.describe("Predefined tests")
def predefined_tests():
    @test.it("Sample test cases")
    def test_assertions():
        do_test([7, 3, 2], 0) # Not triangle
        do_test([2, 4, 6], 0) # Not triangle
        do_test([8, 5, 7], 1) # Acute
        do_test([3, 4, 5], 2) # Right
        do_test([7, 12, 8], 3) # Obtuse
