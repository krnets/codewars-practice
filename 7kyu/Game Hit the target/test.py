import codewars_test as test
from kata import solution

test.assert_equals(solution([
  ['>', ' '],
  [' ', 'x']
]), False)

test.assert_equals(solution([
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', '>', ' ', 'x'],
  [' ', ' ', '', ' ', ' ']
]), True)