using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("20th", Kata.WhatCentury("1999"), "With input '1999' solution produced wrong output.");
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("21st", Kata.WhatCentury("2011"), "With input '2011' solution produced wrong output.");
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("22nd", Kata.WhatCentury("2154"), "With input '2154' solution produced wrong output.");
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("23rd", Kata.WhatCentury("2259"), "With input '2259' solution produced wrong output.");
    }
    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual("20th", Kata.WhatCentury("2000"));
    }
}