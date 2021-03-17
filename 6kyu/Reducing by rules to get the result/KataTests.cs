using NUnit.Framework;
using System;

public class KataTests
{
    [Test]
    public void ExampleTests()
    {
        Func<double, double, double>[] rules = new Func<double, double, double>[]
        {
            (a, b) => a + b,
            (a, b) => a - b
        };

        Assert.AreEqual(5.0, Kata.ReduceByRules(new[] {2.0, 2.0, 3.0, 4.0}, rules));

        rules = new Func<double, double, double>[] {(a, b) => a + b};

        Assert.AreEqual(6.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0}, rules));
        Assert.AreEqual(8.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0, 2.0}, rules));
        Assert.AreEqual(10.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0, 2.0, 2.0}, rules));
        Assert.AreEqual(12.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0, 2.0, 2.0, 2.0}, rules));

        rules = new Func<double, double, double>[] {(a, b) => a + b, (a, b) => a - b, (a, b) => a * b};

        Assert.AreEqual(2.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0}, rules));
        Assert.AreEqual(4.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0, 2.0}, rules));
        Assert.AreEqual(6.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0, 2.0, 2.0}, rules));
        Assert.AreEqual(4.0, Kata.ReduceByRules(new[] {2.0, 2.0, 2.0, 2.0, 2.0, 2.0}, rules));

        rules = new Func<double, double, double>[] {(a, b) => Math.Min(a, b), (a, b) => Math.Max(a, b)};

        Assert.AreEqual(3.3, Kata.ReduceByRules(new[] {1.3, 2.0, 3.3}, rules));
        Assert.AreEqual(2.2, Kata.ReduceByRules(new[] {4.1, 2.2, 2.1, 2.5}, rules));
        Assert.AreEqual(8.0, Kata.ReduceByRules(new[] {8.0, 8.1, 4.1, 12.0, 2.0}, rules));
        Assert.AreEqual(2.4, Kata.ReduceByRules(new[] {2.9, 2.8, 2.7, 2.6, 2.5, 2.4}, rules));
    }
}