using NUnit.Framework;

[TestFixture]
public class SequenceTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(50, Sequence.GetScore(1), "GetScore(1) returns a wrong result");
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(150, Sequence.GetScore(2), "GetScore(2) returns a wrong result");
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(300, Sequence.GetScore(3), "GetScore(3) returns a wrong result");
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(500, Sequence.GetScore(4), "GetScore(4) returns a wrong result");
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(750, Sequence.GetScore(5), "GetScore(5) returns a wrong result");
    }
}