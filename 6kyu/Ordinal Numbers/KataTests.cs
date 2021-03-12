using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("st", Kata.Ordinal(1));
    }

    [Test]
    public void BasicTest11()
    {
        Assert.AreEqual("th", Kata.Ordinal(11));
    }

    [Test]
    public void BasicTest111()
    {
        Assert.AreEqual("th", Kata.Ordinal(111));
    }

    [Test]
    public void BasicTest121()
    {
        Assert.AreEqual("st", Kata.Ordinal(121));
    }

    [Test]
    public void BasicTest20()
    {
        Assert.AreEqual("th", Kata.Ordinal(20));
    }

    [Test]
    public void BasicTest52()
    {
        Assert.AreEqual("nd", Kata.Ordinal(52));
    }

    [Test]
    public void BasicTest903()
    {
        Assert.AreEqual("d", Kata.Ordinal(903, true));
    }

    [Test]
    public void BasicTest1191()
    {
        Assert.AreEqual("st", Kata.Ordinal(1191, true));
    }
}