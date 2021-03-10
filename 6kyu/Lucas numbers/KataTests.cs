using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public static void PositiveNumbersTests()
    {
        Assert.AreEqual(2, Lucas.lucasnum(0));
        Assert.AreEqual(1, Lucas.lucasnum(1));
        Assert.AreEqual(11, Lucas.lucasnum(5));
        Assert.AreEqual(123, Lucas.lucasnum(10));
    }

    [Test]
    public static void NegativeNumbersTests()
    {
        Assert.AreEqual(123, Lucas.lucasnum(-10));
        Assert.AreEqual(-11, Lucas.lucasnum(-5));
        Assert.AreEqual(-1, Lucas.lucasnum(-1));
    }
}