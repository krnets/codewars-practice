using System;
using System.Linq;
using NUnit.Framework;

[TestFixture]
public class ComparingTests
{
    private Random rand = new Random((int) DateTime.Now.Ticks);

    private int lastValue = -1;

    private int getRandomValue()
    {
        var i = rand.Next(0, 9);
        lastValue = i;
        return i;
    }

    [Test]
    public void PerformanceTest()
    {
        string actual = "";

        actual = Kata.Performance(getRandomValue);

        Assert.AreEqual(150000, actual.Length);
        Assert.AreEqual((char) (lastValue + 48), actual.Last());
    }
}