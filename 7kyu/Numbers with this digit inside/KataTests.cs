using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(new long[] {0, 0, 0}, Kata.NumbersWithDigitInside(5, 6));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new long[] {1, 6, 6}, Kata.NumbersWithDigitInside(7, 6));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(new long[] {3, 22, 110}, Kata.NumbersWithDigitInside(11, 1));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(new long[] {2, 30, 200}, Kata.NumbersWithDigitInside(20, 0));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(new long[] {9, 286, 5955146588160}, Kata.NumbersWithDigitInside(44, 4));
    }
}