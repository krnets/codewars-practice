using NUnit.Framework;
using System;

[TestFixture]
public class TopsTest
{
    [Test, Description("Should work for basic strings")]
    public void BasicTest()
    {
        Assert.AreEqual(String.Empty, Kata.Tops(String.Empty));
        Assert.AreEqual("2", Kata.Tops("12"));
        Assert.AreEqual("3pgb", Kata.Tops("abcdefghijklmnopqrstuvwxyz12345"));
        Assert.AreEqual("M3pgb", Kata.Tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN"));
    }
}