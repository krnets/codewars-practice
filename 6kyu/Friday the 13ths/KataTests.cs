using NUnit.Framework;

[TestFixture]
public class FridayTheThirteenthsTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("8/13/1999 10/13/2000", Kata.FridayTheThirteenths(1999, 2000));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("6/13/2014 2/13/2015 3/13/2015 11/13/2015", Kata.FridayTheThirteenths(2014, 2015));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("10/13/2000", Kata.FridayTheThirteenths(2000));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("2/13/2139 3/13/2139 11/13/2139", Kata.FridayTheThirteenths(2139));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual("4/13/1979 7/13/1979 6/13/1980 2/13/1981 3/13/1981 11/13/1981",
            Kata.FridayTheThirteenths(1979, 1981));
    }
}