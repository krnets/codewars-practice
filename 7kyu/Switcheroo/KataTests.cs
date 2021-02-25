using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("bac", Kata.Switcheroo("abc"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("bbbacccabbb", Kata.Switcheroo("aaabcccbaaa"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("ccccc", Kata.Switcheroo("ccccc"));
    }
}