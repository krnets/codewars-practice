using NUnit.Framework;

[TestFixture]
public class Basic_Tests
{
    [Test]
    public void BasicTestCase1()
    {
        Assert.AreEqual(6, CodeWars.overTheRoad(1, 3));
    }

    [Test]
    public void BasicTestCase2()
    {
        Assert.AreEqual(4, CodeWars.overTheRoad(3, 3));
    }

    [Test]
    public void BasicTestCase3()
    {
        Assert.AreEqual(5, CodeWars.overTheRoad(2, 3));
    }

    [Test]
    public void BasicTestCase4()
    {
        Assert.AreEqual(8, CodeWars.overTheRoad(3, 5));
    }

    [Test]
    public void BasicTestCase5()
    {
        Assert.AreEqual(16, CodeWars.overTheRoad(7, 11));
    }
}