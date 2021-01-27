using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(1, Kata.UnluckyDays(1586));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(3, Kata.UnluckyDays(1001));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(2, Kata.UnluckyDays(2819));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(2, Kata.UnluckyDays(2792));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(2, Kata.UnluckyDays(2723));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual(1, Kata.UnluckyDays(1909));
    }

    [Test]
    public void BasicTest7()
    {
        Assert.AreEqual(2, Kata.UnluckyDays(1812));
    }

    [Test]
    public void BasicTest8()
    {
        Assert.AreEqual(2, Kata.UnluckyDays(1618));
    }

    [Test]
    public void BasicTest9()
    {
        Assert.AreEqual(1, Kata.UnluckyDays(2132));
    }

    [Test]
    public void BasicTest10()
    {
        Assert.AreEqual(3, Kata.UnluckyDays(2065));
    }
}