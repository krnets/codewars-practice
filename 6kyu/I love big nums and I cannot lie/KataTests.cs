using NUnit.Framework;

[TestFixture]
public class BiggestTest
{
    [Test]
    public void InitialTests()
    {
        Assert.AreEqual("321", Kata.Biggest(new[] {1, 2, 3}));
        Assert.AreEqual("12121", Kata.Biggest(new[] {121, 12}));
        Assert.AreEqual("12812", Kata.Biggest(new[] {12, 128}));
        Assert.AreEqual("505150", Kata.Biggest(new[] {5051, 50}));
        Assert.AreEqual("10110", Kata.Biggest(new[] {10, 101}));
        Assert.AreEqual("9534330", Kata.Biggest(new[] {3, 30, 34, 5, 9}));
    }
}