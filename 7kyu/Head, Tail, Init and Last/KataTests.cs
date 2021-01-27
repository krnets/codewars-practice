using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void TestHead()
    {
        Assert.AreEqual(5, new List<int> {5, 1}.Head());
    }

    [Test]
    public void TestTail()
    {
        Assert.AreEqual(new List<int> {2, 3}, new List<int> {1, 2, 3}.Tail());
    }

    [Test]
    public void TestInit()
    {
        Assert.AreEqual(new List<int> {1, 5, 7}, new List<int> {1, 5, 7, 9}.Init());
    }

    [Test]
    public void TestLast()
    {
        Assert.AreEqual(2, new List<int> {7, 2}.Last_());
    }

    private static readonly Random rnd = new Random();

    [Test, Description("Random Tests")]
    public void RandomTest()
    {
        const int Tests = 100;

        for (int i = 0; i < Tests; ++i)
        {
            List<int> test = new int[rnd.Next(1, 100)].Select(_ => rnd.Next()).ToList();

            Assert.AreEqual(test.First(), test.Head(), "Head failed.");
            Assert.AreEqual(test.Skip(1).ToList(), test.Tail(), "Tail failed.");
            Assert.AreEqual(test.Take(test.Count - 1).ToList(), test.Init(), "Init failed.");
            Assert.AreEqual(test.Last(), test.Last_(), "Last failed.");
        }
    }
}