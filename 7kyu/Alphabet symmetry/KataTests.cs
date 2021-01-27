using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.That(Kata.Solve(new List<string> {"abode", "ABc", "xyzD"}), Is.EqualTo(new List<int> {4, 3, 1}));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.That(Kata.Solve(new List<string> {"abide", "ABc", "xyz"}), Is.EqualTo(new List<int> {4, 3, 0}));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.That(Kata.Solve(new List<string> {"IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"}),
            Is.EqualTo(new List<int> {6, 5, 7}));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.That(Kata.Solve(new List<string> {"encode", "abc", "xyzD", "ABmD"}),
            Is.EqualTo(new List<int> {1, 3, 1, 3}));
    }
}