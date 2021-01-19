using NUnit.Framework;

[TestFixture]
public class palinddromeChainLengthTest
{

    [Test]
    public void Given87OutputShouldBe4()
    {
        Assert.AreEqual(4, Kata.palindromeChainLength(87));
    }
    [Test]
    public void Given89OutputShouldBe24()
    {
        Assert.AreEqual(24, Kata.palindromeChainLength(89));
    }
}