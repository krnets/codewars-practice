using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(5, Kata.pointsNumber(1));
        Assert.AreEqual(13, Kata.pointsNumber(2));
        Assert.AreEqual(29, Kata.pointsNumber(3));
        Assert.AreEqual(81, Kata.pointsNumber(5));
        Assert.AreEqual(3141549, Kata.pointsNumber(1000));
    }
}