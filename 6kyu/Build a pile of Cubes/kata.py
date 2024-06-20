import codewars_test as test


def find_nb(m):
    cube_size = 0
    n = 1
    while cube_size < m:
        cube_size += n**3
        n += 1
    return n - 1 if cube_size == m else -1


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(find_nb(4), -1)
        test.assert_equals(find_nb(16), -1)
        test.assert_equals(find_nb(4183059834009), 2022)
        test.assert_equals(find_nb(24723578342962), -1)
        test.assert_equals(find_nb(135440716410000), 4824)
        test.assert_equals(find_nb(40539911473216), 3568)
        test.assert_equals(find_nb(26825883955641), 3218)
