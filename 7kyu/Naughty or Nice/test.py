import codewars_test as test
from kata import what_list_am_i_on

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
        good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
        actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
        test.assert_equals(what_list_am_i_on(bad_actions), 'naughty')
        test.assert_equals(what_list_am_i_on(good_actions), 'nice')
        test.assert_equals(what_list_am_i_on(actions), 'naughty')