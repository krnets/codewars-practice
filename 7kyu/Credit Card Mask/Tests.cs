using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void ExamplesTest1()
    {
        Assert.AreEqual("############5616", Kata.Maskify("4556364607935616"));
    }

    [Test]
    public void ExamplesTest2()
    {
        Assert.AreEqual("1", Kata.Maskify("1"));
    }

    [Test]
    public void ExamplesTest3()
    {
        Assert.AreEqual("#1111", Kata.Maskify("11111"));
    }
}