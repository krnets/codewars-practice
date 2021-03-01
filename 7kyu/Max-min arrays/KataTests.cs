using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.That(Kata.Solve(new List<int> {15, 11, 10, 7, 12}), Is.EqualTo(new List<int> {15, 7, 12, 10, 11}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.That(Kata.Solve(new List<int> {91, 75, 86, 14, 82}), Is.EqualTo(new List<int> {91, 14, 86, 75, 82}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.That(Kata.Solve(new List<int> {84, 79, 76, 61, 78}), Is.EqualTo(new List<int> {84, 61, 79, 76, 78}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.That(Kata.Solve(new List<int> {52, 77, 72, 44, 74, 76, 40}),
            Is.EqualTo(new List<int> {77, 40, 76, 44, 74, 52, 72}));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.That(Kata.Solve(new List<int> {1, 6, 9, 4, 3, 7, 8, 2}),
            Is.EqualTo(new List<int> {9, 1, 8, 2, 7, 3, 6, 4}));
    }

    [Test]
    public void SampleTest6()
    {
        Assert.That(Kata.Solve(new List<int> {78, 79, 52, 87, 16, 74, 31, 63, 80}),
            Is.EqualTo(new List<int> {87, 16, 80, 31, 79, 52, 78, 63, 74}));
    }
}