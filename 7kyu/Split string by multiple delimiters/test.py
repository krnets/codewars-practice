import codewars_test as test
from kata import multiple_split

test.assert_equals(multiple_split('Hi everybody!', [' ', '!']), ['Hi', 'everybody'])
test.assert_equals(multiple_split('(1+2)*6-3^9', ['+', '-', '(', ')', '^', '*']), ['1', '2', '6', '3', '9'])
test.assert_equals(multiple_split('Solve_this|kata-very\quickly!', ['!', '|', '\\', '_', '-']), ['Solve', 'this', 'kata', 'very', 'quickly'])
test.assert_equals(multiple_split('', []), [])
test.assert_equals(multiple_split(''), [])
test.assert_equals(multiple_split('some strange string'), ['some strange string'])
test.assert_equals(multiple_split('1_2_3_huhuh_hahaha', ['_']), ['1', '2', '3', 'huhuh', 'hahaha'])
test.assert_equals(multiple_split('((1+2))*(6-3)^9', ['+', '-', '(', ')', '^', '*']), ['1', '2', '6', '3', '9'])
test.assert_equals(multiple_split('(((1+2)-(3)))', ['(', ')']), ['1+2', '-', '3'])