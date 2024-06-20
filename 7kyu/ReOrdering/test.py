import codewars_test as test
from kata import re_ordering

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        BASIC_TESTS = [
            ('ming Yao', 'Yao ming'),
            ('Mano donowana', 'Mano donowana'),
            ('wario LoBan hello', 'LoBan wario hello'),
            ('bull color pig Patrick', 'Patrick bull color pig'),
            ('jojo ddjajdiojdwo ana G nnibiial', 'G jojo ddjajdiojdwo ana nnibiial'),
            ('is one of those rare names that s both exotic and simple Adira',
             'Adira is one of those rare names that s both exotic and simple'),
            ('is an older name than annabel Amabel and a lot more distinctive',
             'Amabel is an older name than annabel and a lot more distinctive')
        ]

        for input_str, result in BASIC_TESTS:
            test.assert_equals(re_ordering(input_str), result)
