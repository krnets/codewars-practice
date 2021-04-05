using System;
using NUnit.Framework;

[TestFixture]
public class CodeWarsTest
{
    [Test]
    public void GivenDiscount75Rate25Returns100()
    {
        Assert.AreEqual(100.00M, Kata.DiscoverOriginalPrice(75M, 25M));
    }
}