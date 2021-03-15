using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual("23:59", Solution.solve(new String[] {"14:51"}));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual("09:10", Solution.solve(new String[] {"21:14", "15:34", "14:51", "06:25", "15:30"}));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual("11:40", Solution.solve(new String[] {"23:00", "04:22", "18:05", "06:24"}));
    }
}