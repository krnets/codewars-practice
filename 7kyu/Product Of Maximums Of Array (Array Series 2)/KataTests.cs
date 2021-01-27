using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(20, Kata.MaxProduct(new int[] {4, 3, 5}, 2));
        Assert.AreEqual(720, Kata.MaxProduct(new int[] {10, 8, 7, 9}, 3));
        Assert.AreEqual(288, Kata.MaxProduct(new int[] {8, 6, 4, 6}, 3));
        Assert.AreEqual(9600, Kata.MaxProduct(new int[] {10, 2, 3, 8, 1, 10, 4}, 5));
        Assert.AreEqual(247895375, Kata.MaxProduct(new int[] {13, 12, -27, -302, 25, 37, 133, 155, -14}, 5));
        Assert.AreEqual(4, Kata.MaxProduct(new int[] {-4, -27, -15, -6, -1}, 2));
        Assert.AreEqual(136, Kata.MaxProduct(new int[] {-17, -8, -102, -309}, 2));
        Assert.AreEqual(-30, Kata.MaxProduct(new int[] {10, 3, -27, -1}, 3));
        Assert.AreEqual(-253344, Kata.MaxProduct(new int[] {14, 29, -28, 39, -16, -48}, 4));
        Assert.AreEqual(1, Kata.MaxProduct(new int[] {1}, 1));
    }
}