import codewars_test as test
from kata import array_to_tree, Node


@test.describe("Example tests")
def test_group():
    @test.it("empty array")
    def test_case():
        test.assert_equals(array_to_tree([]), None, "With arr = []")

    @test.it("example array")
    def test_case():
        s_actual = str(array_to_tree([17, 0, -4, 3, 15]))
        s_expected = str(Node(17, Node(0, Node(3), Node(15)), Node(-4)))
        test.assert_equals(
            s_actual,
            s_expected,
            f"With arr = [17, 0, -4, 3, 15]\nExpected\n{s_expected}\nBut got\n{s_actual}",
        )
