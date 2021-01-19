using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(56, Kata.SumTriangularNumbers(6));
    }
    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(7140, Kata.SumTriangularNumbers(34));
    }
    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(0, Kata.SumTriangularNumbers(-291));

    }
    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(140205240, Kata.SumTriangularNumbers(943));
    }
    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(0, Kata.SumTriangularNumbers(-971));
    }
}