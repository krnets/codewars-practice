using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest()
    {
        Assert.AreEqual("Value is 00005", PaddedNumbers.Solution(5));
    }
}