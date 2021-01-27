using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("hue", Kata.Spam(1));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("huehuehuehuehuehue", Kata.Spam(6));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("huehuehuehuehuehuehuehuehuehuehuehuehuehue", Kata.Spam(14));
    }
}