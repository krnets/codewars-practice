using NUnit.Framework;

[TestFixture]
public class NumberTest
{
    private Number num;

    [SetUp]
    public void SetUp()
    {
        num = new Number();
    }

    [TearDown]
    public void TearDown()
    {
        num = null;
    }

    [Test]
    public void Test1()
    {
        Assert.AreEqual(7, num.DigitalRoot(16));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(6, num.DigitalRoot(456));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(2, num.DigitalRoot(992));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(9, num.DigitalRoot(999999999999));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual(9, num.DigitalRoot(167346));
    }

    [Test]
    public void Test6()
    {
        Assert.AreEqual(0, num.DigitalRoot(0));
    }

    [Test]
    public void Test7()
    {
        Assert.AreEqual(1, num.DigitalRoot(10));
    }
}