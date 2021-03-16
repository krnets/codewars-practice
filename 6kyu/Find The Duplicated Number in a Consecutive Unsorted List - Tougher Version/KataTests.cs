using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(1, Kata.FindDup(new[] {1, 2, 3, 1}));
        Assert.AreEqual(1, Kata.FindDup(new[] {5, 4, 3, 2, 1, 1}));
        Assert.AreEqual(5, Kata.FindDup(new[] {1, 3, 2, 5, 4, 5, 7, 6}));
        Assert.AreEqual(2, Kata.FindDup(new[] {8, 2, 6, 3, 7, 2, 5, 1, 4}));
        Assert.AreEqual(1, Kata.FindDup(new[] {1, 1}));
    }
}