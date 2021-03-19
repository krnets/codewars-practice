using NUnit.Framework;

[TestFixture]
public class IntegerTests
{
    [Test]
    public void GenericTest()
    {
        Assert.AreEqual(2, Kata.GetCount(123));
    }

    [Test]
    public void ZeroTest()
    {
        Assert.AreEqual(5, Kata.GetCount(1230));
    }

    [Test]
    public void TwoOnes()
    {
        Assert.AreEqual(2, Kata.GetCount(11));
    }
    [Test]
    public void SingleDigitTest()
    {
        Assert.AreEqual(0, Kata.GetCount(1));
    }

    [Test]
    public void LongIntegerTest()
    {
        Assert.AreEqual(25, Kata.GetCount(1111111111));
    }
}