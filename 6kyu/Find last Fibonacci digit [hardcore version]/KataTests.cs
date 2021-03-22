using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(1, Kata.LastFibDigit(1));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(6, Kata.LastFibDigit(21));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(1, Kata.LastFibDigit(302));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(7, Kata.LastFibDigit(4003));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(8, Kata.LastFibDigit(50004));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual(5, Kata.LastFibDigit(600005));
    }

    [Test]
    public void BasicTest7()
    {
        Assert.AreEqual(3, Kata.LastFibDigit(7000006));
    }

    [Test]
    public void BasicTest8()
    {
        Assert.AreEqual(8, Kata.LastFibDigit(80000007));
    }

    [Test]
    public void BasicTest9()
    {
        Assert.AreEqual(1, Kata.LastFibDigit(900000008));
    }

    [Test]
    public void BasicTest10()
    {
        Assert.AreEqual(9, Kata.LastFibDigit(1000000009));
    }
}