using System;
using NUnit.Framework;

[TestFixture]
public class Tests
{
    Kata k = new Kata();

    [Test]
    public void SimpleNumbersTest1()
    {
        Assert.AreEqual("1", k.Pattern(1));
    }

    [Test]
    public void SimpleNumbersTest2()
    {
        Assert.AreEqual("1\n22", k.Pattern(2));
    }

    [Test]
    public void SimpleNumbersTest3()
    {
        Assert.AreEqual("1\n22\n333\n4444\n55555", k.Pattern(5));
    }
}