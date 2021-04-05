using NUnit.Framework;

[TestFixture]
public class DiagonalSumTests
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(12, Kata.DiagonalSum(new int[,] {{12}}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(5, Kata.DiagonalSum(new int[2, 2] {{1, 2}, {3, 4}}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(15, Kata.DiagonalSum(new int[,] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(34,
            Kata.DiagonalSum(new int[,] {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}}));
    }
}