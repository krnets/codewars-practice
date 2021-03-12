using NUnit.Framework;
using System;

[TestFixture]
public class Sample_Test
{
    [Test]
    public void FormatTest800()
    {
        Assert.AreEqual("8:00", Kata.FormatTime(800));
    }

    [Test]
    public void FormatTest1000()
    {
        Assert.AreEqual("10:00", Kata.FormatTime(1000));
    }

    [Test]
    public void FormatTest1451()
    {
        Assert.AreEqual("14:51", Kata.FormatTime(1451));
    }

    [Test]
    public void FormatTest3351()
    {
        Assert.AreEqual("33:51", Kata.FormatTime(3351));
    }

    [Test]
    public void FormatTest10_000()
    {
        Assert.Throws<ArgumentException>(delegate { Kata.FormatTime(10_000); });
    }

    [Test, Description("Should throw ArgumentException for invalid number")]
    public void ErrorTest()
    {
        Assert.Throws<ArgumentException>(delegate { Kata.FormatTime(80); });
    }
}