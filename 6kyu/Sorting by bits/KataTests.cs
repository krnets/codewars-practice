using NUnit.Framework;

[TestFixture]
class Tests
{
    [Test]
    [TestCase(new[] {3, 8, 3, 6, 5, 7, 9, 1}, new[] {1, 8, 3, 3, 5, 6, 9, 7})]
    [TestCase(new[] {9, 4, 5, 3, 5, 7, 2, 56, 8, 2, 6, 8, 0}, new[] {0, 2, 2, 4, 8, 8, 3, 5, 5, 6, 9, 7, 56})]
    public void BasicTests(int[] input, int[] expected)
    {
        Assert.That(Kata.SortByBit(input), Is.EqualTo(expected));
    }
}