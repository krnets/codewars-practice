using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void EmptyTest()
    {
        Assert.AreEqual("", Kata.UniqueInOrder(""));
    }

    [Test]
    public void Test1()
    {
        Assert.AreEqual("ABCDAB", Kata.UniqueInOrder("AAAABBBCCDAABBB"));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual("aA", Kata.UniqueInOrder("aA"));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual("AD", Kata.UniqueInOrder("ADD"));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual("DA", Kata.UniqueInOrder("DDA"));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual("1232456", Kata.UniqueInOrder("112332444566"));
    }

    [Test]
    public void ListTest1()
    {
        Assert.AreEqual(new List<int> {1, 2, 3}, Kata.UniqueInOrder(new List<int> {1, 2, 3, 3}));
    }

    [Test]
    public void ListTest2()
    {
        Assert.AreEqual(new List<double> {1, 2, 3}, Kata.UniqueInOrder(new List<double> {1, 2, 3, 3}));
    }

    [Test]
    public void ListTest3()
    {
        Assert.AreEqual(new List<char> {'1', '2', '3'}, Kata.UniqueInOrder(new List<char> {'1', '2', '3', '3'}));
    }

    [Test]
    public void ListTest4()
    {
        Assert.AreEqual(new List<string> {"1", "2", "3"}, Kata.UniqueInOrder(new List<string> {"1", "2", "3", "3"}));
    }
}