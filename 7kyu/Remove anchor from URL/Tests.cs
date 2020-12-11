using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("www.codewars.com", Kata.RemoveUrlAnchor("www.codewars.com#about"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("www.codewars.com/katas/?page=1", Kata.RemoveUrlAnchor("www.codewars.com/katas/?page=1#about"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("www.codewars.com/katas/", Kata.RemoveUrlAnchor("www.codewars.com/katas/"));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual("", Kata.RemoveUrlAnchor(""));
    }
}