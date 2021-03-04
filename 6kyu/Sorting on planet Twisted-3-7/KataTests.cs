using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(string.Join(",", new[] {1, 2, 7, 4, 5, 6, 3, 8, 9}),
            string.Join(",", Kata.SortTwisted37(new[] {1, 2, 3, 4, 5, 6, 7, 8, 9})));
        Assert.AreEqual(string.Join(",", new[] {12, 14, 13}),
            string.Join(",", Kata.SortTwisted37(new[] {12, 13, 14})));
        Assert.AreEqual(string.Join(",", new[] {2, 7, 4, 3, 9}),
            string.Join(",", Kata.SortTwisted37(new[] {9, 2, 4, 7, 3})));
    }
}