using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void FixedTest()
    {
        Assert.That(Kata.Lcm(new List<int> {2, 5}), Is.EqualTo(10));
        Assert.That(Kata.Lcm(new List<int> {2, 3, 4}), Is.EqualTo(12));
        Assert.That(Kata.Lcm(new List<int> {9}), Is.EqualTo(9));
    }
}