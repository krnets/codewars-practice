using NUnit.Framework;

[TestFixture]
public class TrailingZeros
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(1, Kata.TrailingZeros(5));
        Assert.AreEqual(6, Kata.TrailingZeros(25));
        Assert.AreEqual(131, Kata.TrailingZeros(531));
    }
}