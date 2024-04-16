import codewars_test as test
from kata import binary_fingers

sample_test_cases = [
    (     '', []),
    (  '101', ['Middle','Thumb']),
    ('11111', ['Pinkie','Ring','Middle','Index','Thumb']),
]

@test.describe('Sample tests')
def sample_tests():
    for bin_string, expected in sample_test_cases:
        @test.it(f'binary_fingers({bin_string!r})')
        def _():
            test.assert_equals(binary_fingers(bin_string), expected)