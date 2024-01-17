from kata import create_dict
import codewars_test as test


@test.describe("Basic tests")
def test_group():
    # Add your tests on specified format:
    # i: ((inp_keys, inp_values), expected)
    tests = {
        0: ((["a", "b", "c", "d"], [1, 2, 3]), {"a": 1, "b": 2, "c": 3, "d": None}),
        1: ((["a", "b", "c"], [1, 2, 3, 4]), {"a": 1, "b": 2, "c": 3}),
    }
    for _, value in tests.items():

        @test.it(
            f"Testing for keys = {value[0][0]}, values= {value[0][1]}, expected = {value[1]}"
        )
        def test_case():
            test.assert_equals(
                create_dict(value[0][0], value[0][1]),
                value[1],
                f"Didnt work for  keys = {value[0][0]}, values= {value[0][1]}",
            )
