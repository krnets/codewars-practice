using NUnit.Framework;

[TestFixture]
public class DigPowTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(1, DigPow.digPow(89, 1));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(-1, DigPow.digPow(92, 1));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(51, DigPow.digPow(46288, 3));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(9, DigPow.digPow(114, 3));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual(-1, DigPow.digPow(46288, 5));
    }

    [Test]
    public void Test6()
    {
        Assert.AreEqual(1, DigPow.digPow(135, 1));
    }

    [Test]
    public void Test7()
    {
        Assert.AreEqual(1, DigPow.digPow(175, 1));
    }

    [Test]
    public void Test8()
    {
        Assert.AreEqual(1, DigPow.digPow(518, 1));
    }

    [Test]
    public void Test9()
    {
        Assert.AreEqual(1, DigPow.digPow(63761, 3));
    }

    [Test]
    public void Test10()
    {
        Assert.AreEqual(1, DigPow.digPow(598, 1));
    }

    [Test]
    public void Test11()
    {
        Assert.AreEqual(1, DigPow.digPow(1306, 1));
    }

    [Test]
    public void Test12()
    {
        Assert.AreEqual(1, DigPow.digPow(2427, 1));
    }

    [Test]
    public void Test13()
    {
        Assert.AreEqual(1, DigPow.digPow(2646798, 1));
    }

    [Test]
    public void Test14()
    {
        Assert.AreEqual(-1, DigPow.digPow(3456789, 1));
    }

    [Test]
    public void Test15()
    {
        Assert.AreEqual(-1, DigPow.digPow(3456789, 5));
    }

    [Test]
    public void Test16()
    {
        Assert.AreEqual(3, DigPow.digPow(198, 1));
    }

    [Test]
    public void Test17()
    {
        Assert.AreEqual(3, DigPow.digPow(249, 1));
    }

    [Test]
    public void Test18()
    {
        Assert.AreEqual(2, DigPow.digPow(1377, 1));
    }

    [Test]
    public void Test19()
    {
        Assert.AreEqual(1, DigPow.digPow(1676, 1));
    }

    [Test]
    public void Test20()
    {
        Assert.AreEqual(2, DigPow.digPow(695, 2));
    }

    [Test]
    public void Test21()
    {
        Assert.AreEqual(19, DigPow.digPow(1878, 2));
    }

    [Test]
    public void Test22()
    {
        Assert.AreEqual(5, DigPow.digPow(7388, 2));
    }

    [Test]
    public void Test23()
    {
        Assert.AreEqual(1, DigPow.digPow(47016, 2));
    }

    [Test]
    public void Test24()
    {
        Assert.AreEqual(1, DigPow.digPow(542186, 2));
    }

    [Test]
    public void Test25()
    {
        Assert.AreEqual(5, DigPow.digPow(261, 3));
    }

    [Test]
    public void Test26()
    {
        Assert.AreEqual(35, DigPow.digPow(1385, 3));
    }

    [Test]
    public void Test27()
    {
        Assert.AreEqual(66, DigPow.digPow(2697, 3));
    }

    [Test]
    public void Test28()
    {
        Assert.AreEqual(10, DigPow.digPow(6376, 3));
    }

    [Test]
    public void Test29()
    {
        Assert.AreEqual(1, DigPow.digPow(6714, 3));
    }

    [Test]
    public void Test30()
    {
        Assert.AreEqual(1, DigPow.digPow(63760, 3));
    }

    [Test]
    public void Test31()
    {
        Assert.AreEqual(4, DigPow.digPow(132921, 3));
    }

    [Test]
    public void Test32()
    {
        Assert.AreEqual(12933, DigPow.digPow(10383, 6));
    }
}