using System;
using NUnit.Framework;

[TestFixture]
public class TriangleNumbersTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(true, TriangleNumbers.isTriangleNumber(125250));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(true, TriangleNumbers.isTriangleNumber(3126250));
    }
}