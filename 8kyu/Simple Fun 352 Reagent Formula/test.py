from kata import isValid
import codewars_test as test


@test.describe('Basic Tests')
def basic_tests():

    @test.it("It should works for basic tests.")
    def basic_test_cases():
        test.assert_equals(isValid([1, 3, 7]), True)
        test.assert_equals(isValid([7, 1, 2, 3]), False)
        test.assert_equals(isValid([1, 3, 5, 7]), False)
        test.assert_equals(isValid([1, 5, 6, 7, 3]), True)
        test.assert_equals(isValid([5, 6, 7]), True)
        test.assert_equals(isValid([5, 6, 7, 8]), True)
        test.assert_equals(isValid([6, 7, 8]), False)
        test.assert_equals(isValid([7, 8]), True)


@test.describe('Ranomized Tests')
def random_tests():

    def reference_solution(formula):
        return not (
            (1 in formula and 2 in formula) or
            (3 in formula and 4 in formula) or
            (5 in formula and not 6 in formula) or
            (not 5 in formula and 6 in formula) or
            (not 7 in formula and not 8 in formula))

    import itertools as it
    from random import shuffle
    lst = list(range(1, 9))
    test_cases = [perm for sublist in [[list(y) for y in x] for x in [list(
        it.combinations(lst, n)) for n in range(1, len(lst))]] for perm in sublist]
    shuffle(test_cases)

    for test_case in test_cases:
        valid = reference_solution(test_case)
        validstr = "valid" if valid else "invalid"

        @test.it(f"{test_case} is {validstr}")
        def random_test_cases():
            test.assert_equals(isValid(test_case), valid)
