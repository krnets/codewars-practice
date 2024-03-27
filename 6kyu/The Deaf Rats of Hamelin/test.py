from kata import count_deaf_rats
import codewars_test as test


@test.it("ex1")
def ex1():
    test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0)


@test.it("ex2")
def ex2():
    test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1)


@test.it("ex3")
def ex3():
    test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)
