using NUnit.Framework;

[TestFixture]
public class NextBiggerNumberTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(21, Kata.NextBiggerNumber(12));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(531, Kata.NextBiggerNumber(513));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(2071, Kata.NextBiggerNumber(2017));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(441, Kata.NextBiggerNumber(414));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual(414, Kata.NextBiggerNumber(144));
    }
}