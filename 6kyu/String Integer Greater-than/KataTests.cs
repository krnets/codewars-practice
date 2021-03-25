using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.IsFalse(Kata.StringIntGreaterThan("31", "162"));
        Assert.IsFalse(Kata.StringIntGreaterThan("16", "162"));
        Assert.IsTrue(Kata.StringIntGreaterThan("162", "54"));
    }
}