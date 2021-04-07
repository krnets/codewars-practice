using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SumOfKTests
{
    [Test]
    public void Test1()
    {
        List<int> ts = new List<int> {50, 55, 56, 57, 58};
        int? n = SumOfK.chooseBestSum(163, 3, ts);
        Assert.AreEqual(163, n);
    }

    [Test]
    public void Test2()
    {
        var ts = new List<int> {50};
        var n = SumOfK.chooseBestSum(163, 3, ts);
        Assert.AreEqual(null, n);
    }

    [Test]
    public void Test3()
    {
        var ts = new List<int> {91, 74, 73, 85, 73, 81, 87};
        var n = SumOfK.chooseBestSum(230, 3, ts);
        Assert.AreEqual(228, n);
    }
}