using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test, Description("tests for counting the length of a linked list.")]
    public void LengthTest()
    {
        Node list = Node.BuildOneTwoThree();
        Assert.AreEqual(0, Node.Length(null), "Length of null list should be zero.");
        Assert.AreEqual(1, Node.Length(new Node(99)), "Length of single node list should be one.");
        Assert.AreEqual(3, Node.Length(list), "Length of the three node list should be three.");
    }

    [Test, Description("tests for counting occurences of data that satisfies a condition.")]
    public void CountTest()
    {
        Node list = Node.BuildOneTwoThree();
        Assert.AreEqual(1, Node.Count(list, value => value == 1), "list should only contain one 1.");
        Assert.AreEqual(1, Node.Count(list, value => value == 2), "list should only contain one 2.");
        Assert.AreEqual(1, Node.Count(list, value => value == 3), "list should only contain one 3.");
        Assert.AreEqual(0, Node.Count(list, value => value == 99),
            "list should return zero for integer not found in list.");
        Assert.AreEqual(0, Node.Count(null, value => value == 1), "null list should always return count of zero.");

        Assert.AreEqual(2, Node.Count(list, value => value % 2 != 0), "list should contain two odd numbers.");
        Assert.AreEqual(1, Node.Count(list, value => value % 2 == 0), "list should contain one even number.");
    }
}