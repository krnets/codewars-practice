using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class GreatestDistanceTests
{
    [Test]
    public void FirstCase()
    {
        Assert.AreEqual(GreatestDistance.Exec(new List<int> {9, 7, 1, 2, 3, 7, 0, -1, -2}), 4);
    }

    [Test]
    public void SecondCase()
    {
        Assert.AreEqual(GreatestDistance.Exec(new List<int> {0, 7, 0, 2, 3, 7, 0, -1, -2}), 6);
    }

    [Test]
    public void ThirdCase()
    {
        Assert.AreEqual(GreatestDistance.Exec(new List<int> {1, 2, 3, 4}), 0);
    }
}