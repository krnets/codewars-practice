import codewars_test as test
from kata import insert_nth, Node

def build_one_two_three():
    return Node(1, Node(2, Node(3)))

@test.describe("Tests")
def tes():

    @test.it("should be able to handle an empty list.")
    def f():
        test.assert_equals(insert_nth(None, 0, 12).data, 12, "should be able to insert a node on an empty/None list.")
        test.assert_equals(insert_nth(None, 0, 12).next, None, "value at index 1 should be None.")

    @test.it("should be able to insert a new node at the head of a list.")
    def f():
        test.assert_equals(insert_nth(build_one_two_three(), 0, 23).data, 23, "should be able to insert new node at head of list.")
        test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.data, 1, "value for node at index 1 should be 1.")
        test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.data, 2, "value for node at index 2 should be 2.")
        test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
        test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.next.next, None, "value at index 4 should be None.")

    @test.it("should be able to insert a new node at index 1 of a list.")
    def f():
        test.assert_equals(insert_nth(build_one_two_three(), 1, 23).data, 1, "value for node at index 0 should be 1.")
        test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.data, 23, "value for node at index 1 should be 23")
        test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.data, 2, "value for node at index 2 should be 2.")
        test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
        test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.next.next, None, "value at index 4 should be None.")

    @test.it("should be able to insert a new node at index 2 of a list.")
    def f():
        test.assert_equals(insert_nth(build_one_two_three(), 2, 23).data, 1, "head should remain unchanged after inserting new node at index 2")
        test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.data, 2, "value at index 1 should remain unchanged after inserting new node at index 2")
        test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.data, 23, "value for node at index 2 should be 23.")
        test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
        test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.next.next, None, "value at index 4 should be None.")

    @test.it("should be able to insert a new node at tail of a list.")
    def f():
        test.assert_equals(insert_nth(build_one_two_three(), 3, 23).data, 1, "head should remain unchanged after inserting new node at tail")
        test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.data, 2, "value at index 1 should remain unchanged after inserting new node at tail")
        test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.data, 3, "value for node at index 2 should be 3.")
        test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.next.data, 23, "value for node at index 3 should be 23.")
        test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.next.next, None, "value at index 4 should be None.")

    @test.it("should raise exception if index is too large.")
    def f():
        test.expect_error("Invalid index value should raise error.", lambda : insert_nth(build_one_two_three(), 4, 23))