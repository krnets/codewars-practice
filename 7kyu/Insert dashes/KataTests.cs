using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("4547-9-3", Kata.InsertDash(454793));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("123456", Kata.InsertDash(123456));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("1003-567", Kata.InsertDash(1003567));
    }
}