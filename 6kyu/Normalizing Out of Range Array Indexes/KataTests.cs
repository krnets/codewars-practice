using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTesPositive()
    {
        int[] array = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        Assert.AreEqual(1, Kata.NormIndex(array, 11));
    }

    [Test]
    public void SampleTestNegative()
    {
        int[] array = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        Assert.AreEqual(1, Kata.NormIndex(array, -9));
    }
}