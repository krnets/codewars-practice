using NUnit.Framework;
using System;
using System.Text;
using System.Text.RegularExpressions;

[TestFixture]
public class KataTestf
{
    [Test]
    public void _0_BasicTests()
    {
        var kata = new Kata();

        Assert.AreEqual("abc", kata.CreateSequence(new Regex(@"[a-c]")));
        Assert.AreEqual("0123456789ABCDEF", kata.CreateSequence(new Regex(@"[0-9A-F]")));
    }
}