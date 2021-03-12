using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(5, Kata.NthSmallest(new int[][] {new int[] {1, 5}, new int[] {2}, new int[] {4, 8, 9}}, 4));
    }
}