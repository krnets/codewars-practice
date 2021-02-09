using NUnit.Framework;

public class SolutionTest
{
    [Test]
    public void FixedTest()
    {
        // Basic tests
        int[] test = {1, 2, 3, 4, 5};
        int[] a1 = {15}, a2 = {9, 6}, a3 = {5, 7, 3}, a4 = {1, 2, 3, 4, 5, 0}, a5 = { };
        Assert.AreEqual(a1, Kata.Beggars(test, 1));
        Assert.AreEqual(a2, Kata.Beggars(test, 2));
        Assert.AreEqual(a3, Kata.Beggars(test, 3));
        Assert.AreEqual(a4, Kata.Beggars(test, 6));
        Assert.AreEqual(a5, Kata.Beggars(test, 0));
    }
}