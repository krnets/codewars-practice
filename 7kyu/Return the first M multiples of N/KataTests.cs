using NUnit.Framework;
using System;

[TestFixture]
public class Test
{
    [Test]
    public void SampleTests()
    {
        Assert.AreEqual(new double[] {5, 10, 15}, Kata.Multiples(3, 5));
    }
}