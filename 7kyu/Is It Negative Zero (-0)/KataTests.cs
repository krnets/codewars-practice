using NUnit.Framework;

[TestFixture, Description("Basic Tests")]
public class BasicTests
{
    [Test, Description("should return true for -0")]
    public void Test1()
    {
        Assert.AreEqual(true, Kata.IsNegativeZero(-0.0));
    }

    [Test, Description("should return false for non-negative-zero numbers")]
    public void Test2()
    {
        Assert.AreEqual(false, Kata.IsNegativeZero(double.NegativeInfinity));
        Assert.AreEqual(false, Kata.IsNegativeZero(-5.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(-4.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(-3.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(-2.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(-1.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(-double.MaxValue));
        Assert.AreEqual(false, Kata.IsNegativeZero(0.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(-double.MinValue));
        Assert.AreEqual(false, Kata.IsNegativeZero(1.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(2.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(3.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(4.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(5.0));
        Assert.AreEqual(false, Kata.IsNegativeZero(double.PositiveInfinity));
    }
}