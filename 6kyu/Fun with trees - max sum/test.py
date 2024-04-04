import codewars_test as test
from kata import max_sum, TreeNode

@test.describe("Sample Tests")
def test_group():
    
    def test_it(tree, expected):
        actual = max_sum(tree)
        if actual == expected:
            test.pass_()
        else:
            test.fail(f"Test failed.\n\n   expected: {expected}\ninstead got: {actual}\n\nfor the tree:\n{tree}")
    
    @test.it("Empty Tree")
    def test_case():
        test_it(None, 0)

    @test.it("Perfect Tree")
    def test_case():
        #      5
        #    /   \
        #  -22    11
        #  / \    / \
        # 9  50  9   2
        tree = TreeNode(5,
                 TreeNode(-22,
                   TreeNode(9),
                   TreeNode(50)),
                 TreeNode(11,
                   TreeNode(9),
                   TreeNode(2)))
        test_it(tree, 33)

    @test.it("Unbalanced Tree")
    def test_case():
        tree = TreeNode(6,
                 TreeNode(50,
                   TreeNode(-100),
                   TreeNode(-10)),
                 TreeNode(40))
        test_it(tree, 46)
        
    @test.it("Computes all the way down to leaves")
    def test_case():
        #         5
        #       /   \
        #    4        10
        #   /  \     /
        # -80  -60 -90 
        tree = TreeNode(5,
                 TreeNode(4,
                   TreeNode(-80),
                   TreeNode(-60)),
                 TreeNode(10,
                   TreeNode(-90),
                   None))
        test_it(tree, -51)