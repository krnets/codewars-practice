from kata import partition
import codewars_test as test

animals = ["cat", "dog", "duck", "cow", "donkey"]
test.describe("partition")
test.assert_equals(partition(animals, lambda x: len(x) == 3), (['cat', 'dog', 'cow'], ['duck', 'donkey']))
test.assert_equals(partition(animals, lambda x: x[0] == 'c'), (['cat', 'cow'], ['dog', 'duck', 'donkey']))
test.assert_equals(partition([], lambda x: len(x) == 3), ([], []))