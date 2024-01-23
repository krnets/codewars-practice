from kata import replace_nth
import codewars_test as test

@test.it("Basic Tests")
def _():

    tests = [
        # [expected, [input_args]],
        ["Vader soid: No, I am your fother!", ["Vader said: No, I am your father!", 2, 'a', 'o']],
        ["Vader said: No, I am your fother!", ["Vader said: No, I am your father!", 4, 'a', 'o']],
        ["Vader said: No, I am your father!", ["Vader said: No, I am your father!", 6, 'a', 'o']],
        ["Vader said: No, I am your father!", ["Vader said: No, I am your father!", 0, 'a', 'o']],
        ["Vader said: No, I am your father!", ["Vader said: No, I am your father!", -2, 'a', 'o']],
        ["Vader sayd: No, I am your father!", ["Vader said: No, I am your father!", 1, 'i', 'y']],
        ["Luke cries: Noooooioooooioooo!", ["Luke cries: Noooooooooooooooo!", 6, 'o', 'i']],
    ]

    for exp, inp in tests:
        test.assert_equals(replace_nth(*inp), exp)