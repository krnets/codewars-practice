import codewars_test as test
from kata import calculate_damage


test.assert_equals(calculate_damage("fire", "water", 100, 100), 25)
test.assert_equals(calculate_damage("grass", "water", 100, 100), 100)
test.assert_equals(calculate_damage("electric", "fire", 100, 100), 50)
test.assert_equals(calculate_damage("grass", "electric", 57, 19), 150)
test.assert_equals(calculate_damage("grass", "water", 40, 40), 100)
test.assert_equals(calculate_damage("grass", "fire", 35, 5), 175)
test.assert_equals(calculate_damage("fire", "electric", 10, 2), 250)