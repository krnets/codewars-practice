using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(-16, Kata.LargestPairSum(new int[] {-8, -8, -16, -18, -19}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(0, Kata.LargestPairSum(new int[] {-100, -29, -24, -19, 19}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(10, Kata.LargestPairSum(new int[] {1, 2, 3, 4, 6, -1, 2}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(42, Kata.LargestPairSum(new int[] {10, 14, 2, 23, 19}));
    }
}