using System;
using System.Linq;
using NUnit.Framework;

[TestFixture]
public class ShadesOfGreyTests
{
    [Test]
    public void WithNegativeShouldReturnEmpty()
    {
        CollectionAssert.IsEmpty(Kata.ShadesOfGrey(-1));
    }

    [Test]
    public void WithZeroShouldReturnEmpty()
    {
        CollectionAssert.IsEmpty(Kata.ShadesOfGrey(0));
    }

    [Test]
    public void WithOneShouldReturn010101()
    {
        CollectionAssert.AreEquivalent(new[] {"#010101"}, Kata.ShadesOfGrey(1));
    }

    [Test]
    public void With10ShouldReturn10()
    {
        CollectionAssert.AreEquivalent(
            new[]
            {
                "#010101", "#020202", "#030303", "#040404", "#050505",
                "#060606", "#070707", "#080808", "#090909", "#0a0a0a"
            },
            Kata.ShadesOfGrey(10));
    }

    [Test]
    public void With255ShouldStillReturn254()
    {
        Assert.AreEqual(254, Kata.ShadesOfGrey(255).Length);
    }
}