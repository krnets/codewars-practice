using System;
using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(new int[] {1, 2, 3}, Kata.digitize(123));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(new int[] {1}, Kata.digitize(1));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(new int[] {0}, Kata.digitize(0));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(new int[] {1, 2, 3, 0}, Kata.digitize(1230));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual(new int[] {8, 6, 7, 5, 3, 0, 9}, Kata.digitize(8675309));
    }
}