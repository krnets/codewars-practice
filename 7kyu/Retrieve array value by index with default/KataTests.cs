using NUnit.Framework;
using System;
using System.Linq;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        int[] range = Enumerable.Range(1, 3).ToArray();
        Assert.AreEqual(2, Kata.Solution(range, 1, -1));
    }

    [Test]
    public void SampleTest2()
    {
        int[] range = Enumerable.Range(1, 3).ToArray();
        Assert.AreEqual(3, Kata.Solution(range, -1, -1));
    }

    [Test]
    public void SampleTest3()
    {
        int[] range = Enumerable.Range(1, 3).ToArray();
        Assert.AreEqual(-1, Kata.Solution(range, -5, -1));
    }

    [Test]
    public void SampleTest4()
    {
        int[] range = Enumerable.Range(1, 3).ToArray();
        Assert.AreEqual(1, Kata.Solution(range, -3, -1));
    }
}