using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void FixedTest1()
    {
        Assert.AreEqual("FFFFFF", Kata.Rgb(255, 255, 255));
    }

    [Test]
    public void FixedTest2()
    {
        Assert.AreEqual("FFFFFF", Kata.Rgb(255, 255, 300));
    }

    [Test]
    public void FixedTest3()
    {
        Assert.AreEqual("000000", Kata.Rgb(0, 0, 0));
    }

    [Test]
    public void FixedTest4()
    {
        Assert.AreEqual("9400D3", Kata.Rgb(148, 0, 211));
    }

    [Test]
    public void FixedTest5()
    {
        Assert.AreEqual("9400D3", Kata.Rgb(148, -20, 211), "Handle negative numbers.");
    }

    [Test]
    public void FixedTest6()
    {
        Assert.AreEqual("90C3D4", Kata.Rgb(144, 195, 212));
    }

    [Test]
    public void FixedTest7()
    {
        Assert.AreEqual("D4350C", Kata.Rgb(212, 53, 12), "Consider single hex digit numbers.");
    }
}