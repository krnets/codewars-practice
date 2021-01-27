using NUnit.Framework;
using System;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(new List<int> {9, 10}, Kata.Largest(2, new List<int> {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(new List<int> {5, 5, 5}, Kata.Largest(3, new List<int> {5, 1, 5, 2, 3, 1, 2, 3, 5}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(new List<int> {3, 5, 9, 13, 22, 50, 63},
            Kata.Largest(7, new List<int> {9, 1, 50, 22, 3, 13, 2, 63, 5}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(new List<int> { }, Kata.Largest(0, new List<int> {1, 2, 3, 4, 8, 7, 6, 5}));
    }
}