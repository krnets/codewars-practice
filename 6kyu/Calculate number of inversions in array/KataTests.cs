using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(0, Kata.CountInversions(new int[] {1, 2, 3}), "Sorted array has 0 inversions");
        Assert.AreEqual(1, Kata.CountInversions(new int[] {2, 1, 3}), "Array [2,1,3] only has one inversion");
        Assert.AreEqual(1, Kata.CountInversions(new int[] {1, 3, 2, 4}));
        Assert.AreEqual(3, Kata.CountInversions(new int[] {4, 1, 2, 3}));
        Assert.AreEqual(6, Kata.CountInversions(new int[] {4, 3, 2, 1}));
    }
}