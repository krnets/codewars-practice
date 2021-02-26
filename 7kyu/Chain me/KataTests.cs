using NUnit.Framework;
using System;

[TestFixture]
public class ChainTests
{
    public static double add(double x)
    {
        return x + 10;
    }

    public static double mul(double x)
    {
        return x * 30;
    }

    [Test]
    public static void ExampleTest()
    {
        Assert.AreEqual(Kata.Chain(2, new[] {(Func<double, double>) add, mul}), 360, "Incorrect Value for '2'");
    }
}