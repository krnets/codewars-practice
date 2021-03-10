using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(11.691, Calculator.AreaOfPolygonInsideCircle(3, 3));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(8, Calculator.AreaOfPolygonInsideCircle(2, 4));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(14.86, Calculator.AreaOfPolygonInsideCircle(2.5, 5));
    }
}