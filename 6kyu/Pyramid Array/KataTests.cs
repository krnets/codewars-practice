using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(new int[][] { }, Kata.Pyramid(0));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new int[][] {new int[] {1}}, Kata.Pyramid(1));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(new int[][] {new int[] {1}, new int[] {1, 1}}, Kata.Pyramid(2));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(new int[][] {new int[] {1}, new int[] {1, 1}, new int[] {1, 1, 1}}, Kata.Pyramid(3));
    }
}