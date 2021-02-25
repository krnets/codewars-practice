using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(1, Kata.SumOfABeach("SanD"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(1, Kata.SumOfABeach("sunshine"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(4, Kata.SumOfABeach("sunsunsunsun"));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(1, Kata.SumOfABeach("123FISH321"));
    }
}