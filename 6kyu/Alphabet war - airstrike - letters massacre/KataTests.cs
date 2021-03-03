using NUnit.Framework;
using System;

[TestFixture]
public class AlphabetWarTest
{
    [Test]
    public void BasicTest()
    {
        Assert.AreEqual("Right side wins!", Kata.AlphabetWar("z"));
        Assert.AreEqual("Let's fight again!", Kata.AlphabetWar("****"));
        Assert.AreEqual("Let's fight again!", Kata.AlphabetWar("z*dq*mw*pb*s"));
        Assert.AreEqual("Let's fight again!", Kata.AlphabetWar("zdqmwpbs"));
        Assert.AreEqual("Right side wins!", Kata.AlphabetWar("zz*zzs"));
        Assert.AreEqual("Left side wins!", Kata.AlphabetWar("*wwwwww*z*"));
    }
}