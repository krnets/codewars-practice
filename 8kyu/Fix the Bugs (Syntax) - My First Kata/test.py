from kata import my_first_kata
import codewars_test as test

test.describe("Basic Tests")
test.assert_equals(my_first_kata(3,5),(3 % 5 + 5 % 3))
test.assert_equals(my_first_kata("hello",3),False)
test.assert_equals(my_first_kata(67,"bye"),False)
test.assert_equals(my_first_kata(True,True),False)
test.assert_equals(my_first_kata(314,107),(107 % 314 + 314 % 107))
test.assert_equals(my_first_kata(1,32),(1 % 32 + 32 % 1))
test.assert_equals(my_first_kata(-1,-1),(-1 % -1 + -1 % -1))
test.assert_equals(my_first_kata(19483,9),(9 % 19483 + 19483 % 9))
test.assert_equals(my_first_kata("hello",{}),False)
test.assert_equals(my_first_kata([],"pippi"),False)