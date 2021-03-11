using NUnit.Framework;

public class ExampleTests
{
    [Test]
    public void TestBob27Male()
    {
        var dm = new Dinglemouse().SetName("Bob").SetAge(27).SetSex('M');
        var expected = "Hello. My name is Bob. I am 27. I am male.";
        Assert.AreEqual(expected, dm.Hello());
    }

    [Test]
    public void Test27MaleBob()
    {
        var dm = new Dinglemouse().SetAge(27).SetSex('M').SetName("Bob");
        var expected = "Hello. I am 27. I am male. My name is Bob.";
        Assert.AreEqual(expected, dm.Hello());
    }

    [Test]
    public void TestAliceFemale()
    {
        var dm = new Dinglemouse().SetName("Alice").SetSex('F');
        var expected = "Hello. My name is Alice. I am female.";
        Assert.AreEqual(expected, dm.Hello());
    }

    [Test]
    public void TestBatman()
    {
        var dm = new Dinglemouse().SetName("Batman");
        var expected = "Hello. My name is Batman.";
        Assert.AreEqual(expected, dm.Hello());
    }


    [Test]
    public void TestNoneSet()
    {
        var dm = new Dinglemouse();
        var expected = "Hello.";
        Assert.AreEqual(expected, dm.Hello());
    }

    [Test]
    public void TestMultipleAge()
    {
        var dm = new Dinglemouse().SetAge(25).SetName("Sally").SetAge(39);
        var expected = "Hello. I am 39. My name is Sally.";
        Assert.AreEqual(expected, dm.Hello());
    }

    [Test]
    public void TestMultipleName()
    {
        var dm = new Dinglemouse().SetAge(25).SetName("Sally").SetSex('F').SetName("Betty");
        var expected = "Hello. I am 25. My name is Betty. I am female.";
        Assert.AreEqual(expected, dm.Hello());
    }

    [Test]
    public void TestMultipleSex()
    {
        var dm = new Dinglemouse().SetAge(52).SetSex('F').SetName("Dick").SetSex('M');
        var expected = "Hello. I am 52. I am male. My name is Dick.";
        Assert.AreEqual(expected, dm.Hello());
    }
}