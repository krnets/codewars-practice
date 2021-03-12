using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(0, Kata.DeadAntCount("ant ant ant ant"));
        Assert.AreEqual(0, Kata.DeadAntCount(null));
        Assert.AreEqual(2, Kata.DeadAntCount("ant anantt aantnt"));
        Assert.AreEqual(1, Kata.DeadAntCount("ant ant .... a nt"));
    }
}