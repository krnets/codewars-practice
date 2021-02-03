using NUnit.Framework;
using System;

[TestFixture]
public class DinglemouseTests
{
    [Test]
    public void BasicTest()
    {
        string expected =
            "6|##### 5\n" +
            "5|\n" +
            "4|# 1\n" +
            "3|########## 10\n" +
            "2|### 3\n" +
            "1|####### 7\n";
        Assert.AreEqual(expected, 
            Dinglemouse.Histogram(new int[] {7, 3, 10, 1, 0, 5}));
    }
}