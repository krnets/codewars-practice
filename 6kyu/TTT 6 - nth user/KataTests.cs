using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("1", Kata.UserNumber(1));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("5", Kata.UserNumber(4));
    }

    [Test]
    public void BasicTest8()
    {
        Assert.AreEqual("10", Kata.UserNumber(8));
    }

    [Test]
    public void BasicTest10()
    {
        Assert.AreEqual("12", Kata.UserNumber(10));
    }

    [Test]
    public void BasicTest20()
    {
        Assert.AreEqual("25", Kata.UserNumber(20));
    }

    [Test]
    public void BasicTest500()
    {
        Assert.AreEqual("875", Kata.UserNumber(500));
    }

    [Test]
    public void BasicTest1000()
    {
        Assert.AreEqual("1860", Kata.UserNumber(1000));
    }

    [Test]
    public void BasicTest100000()
    {
        Assert.AreEqual("303250", Kata.UserNumber(100000));
    }
}