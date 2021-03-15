using NUnit.Framework;

[TestFixture]
public class SumSqTest
{
    [Test]
    public void ExampleTest36()
    {
        Assert.AreEqual(36, SqNum.solve(13));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(1, SqNum.solve(3));
    }

    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual(-1, SqNum.solve(1));
        Assert.AreEqual(-1, SqNum.solve(2));
        Assert.AreEqual(-1, SqNum.solve(4));
        Assert.AreEqual(4, SqNum.solve(5));
        Assert.AreEqual(9, SqNum.solve(7));
        Assert.AreEqual(1, SqNum.solve(8));
        Assert.AreEqual(16, SqNum.solve(9));
        Assert.AreEqual(-1, SqNum.solve(10));
        Assert.AreEqual(25, SqNum.solve(11));
        Assert.AreEqual(64, SqNum.solve(17));
        Assert.AreEqual(5428900, SqNum.solve(88901));
        Assert.AreEqual(429235524, SqNum.solve(290101));
    }
}