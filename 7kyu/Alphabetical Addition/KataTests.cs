using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual('f', Kata.AddLetters(new char[] { 'a', 'b', 'c' }));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual('z', Kata.AddLetters(new char[] { 'z' }));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual('c', Kata.AddLetters(new char[] { 'a', 'b' }));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual('c', Kata.AddLetters(new char[] { 'c' }));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual('a', Kata.AddLetters(new char[] { 'z', 'a' }));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual('d', Kata.AddLetters(new char[] { 'y', 'c', 'b' }));
    }

    [Test]
    public void BasicTest7()
    {
        Assert.AreEqual('z', Kata.AddLetters(new char[] { }));
    }
}