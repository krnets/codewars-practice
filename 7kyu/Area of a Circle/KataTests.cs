using System;
using NUnit.Framework;

[TestFixture]
public class AreaOfCircleTests
{
    [Test]
    public void ShouldFailNegativeNumber()
    {
        Assert.Throws<ArgumentException>(delegate { Kata.CalculateAreaOfCircle("-123"); });
        //Assert.Throws(typeof(ArgumentException), Kata.CalculateAreaOfCircle("-123"));
    }

    [Test]
    public void ShouldFailAlphaNumeric()
    {
        Assert.Throws<ArgumentException>(delegate { Kata.CalculateAreaOfCircle("number"); });
    }

    [Test]
    public void ShouldPass1()
    {
        Assert.AreEqual(5881.25, Kata.CalculateAreaOfCircle("43.2673"));
    }
}