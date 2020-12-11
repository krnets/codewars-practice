using System;
using NUnit.Framework;

[TestFixture]
public class NthSeriesTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual("0.00", NthSeries.seriesSum(0));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual("1.77", NthSeries.seriesSum(9));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual("1.94", NthSeries.seriesSum(15));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual("2.26", NthSeries.seriesSum(39));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual("2.40", NthSeries.seriesSum(58));
    }
}