using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(15, Kata.Repeats(new List<int> {4, 5, 7, 5, 4, 8}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(19, Kata.Repeats(new List<int> {9, 10, 19, 13, 19, 13}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(12, Kata.Repeats(new List<int> {16, 0, 11, 4, 8, 16, 0, 11}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(22, Kata.Repeats(new List<int> {5, 17, 18, 11, 13, 18, 11, 13}));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual(24, Kata.Repeats(new List<int> {5, 10, 19, 13, 10, 13}));
    }
}