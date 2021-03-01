using System;
using NUnit.Framework;

[TestFixture]
public class KataTest
{
    private Random random = new Random();
    private Kata kata = new Kata();

    [Test]
    public void Mutate100()
    {
        Assert.AreEqual("1111", kata.Mutate("0000", 1));
        Assert.AreEqual("0000", kata.Mutate("1111", 1));
    }

    [Test]
    public void Mutate0()
    {
        Assert.AreEqual("0000", kata.Mutate("0000", 0));
        Assert.AreEqual("1111", kata.Mutate("1111", 0));
    }
}