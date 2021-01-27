using System;
using NUnit.Framework;

[TestFixture]
public class Tests
{
    Kata k = new Kata();

    [Test]
    public void SimpleNumbers1()
    {
        Assert.AreEqual("1", k.Pattern(1));
    }

    [Test]
    public void SimpleNumbers2()
    {
        Assert.AreEqual("21\n2", k.Pattern(2));
    }

    [Test]
    public void SimpleNumbers3()
    {
        Assert.AreEqual("54321\n5432\n543\n54\n5", k.Pattern(5));
    }
}