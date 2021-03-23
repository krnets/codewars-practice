using NUnit.Framework;

[TestFixture]
public class Pattern12Tests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("1   1\n 2 2 \n  3  \n 2 2 \n1   1", Pattern12.Pattern(3));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(
            "1       1\n 2     2 \n  3   3  \n   4 4   \n    5    \n   4 4   \n  3   3  \n 2     2 \n1       1",
            Pattern12.Pattern(5));
    }
}