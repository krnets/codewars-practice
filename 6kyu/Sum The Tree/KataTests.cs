using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class BasicTest
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(new Node(10, new Node(1), new Node(2))).Returns(13)
                .SetDescription("Simple Test");
            yield return new TestCaseData(new Node(11, new Node(0), new Node(0, null, new Node(1)))).Returns(12)
                .SetDescription("Handles unbalanced trees");
            yield return new TestCaseData(new Node(1)).Returns(1).SetDescription("Handles childless roots");
            yield return new TestCaseData(new Node(-1, null, new Node(-2, null, new Node(-3)))).Returns(-6)
                .SetDescription("Correctly sums negative numbers");
            yield return new TestCaseData(new Node(1, null,
                    new Node(1, null,
                        new Node(1, null, new Node(1, null, new Node(1, null, new Node(1, null, new Node(1))))))))
                .Returns(7).SetDescription("Handles deep nodes");
        }
    }

    [Test, TestCaseSource("testCases")]
    public int Test(Node root) =>
        Kata.SumTree(root);
}