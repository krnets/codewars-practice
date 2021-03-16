using NUnit.Framework;
using System;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTests()
    {
        var kata = new Kata();

        Assert.AreEqual(9, kata.SquareDigitsSequence(16));

        Assert.AreEqual(4, kata.SquareDigitsSequence(103));

        Assert.AreEqual(2, kata.SquareDigitsSequence(1));
    }
}