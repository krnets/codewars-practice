using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(4, Kata.MatchArrays(new int[] {1, 2, 3, 4, 5}, new int[] {2, 3, 4, 5, 6}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(2, Kata.MatchArrays(new int[] {1, 2, 3, 4, 5}, new int[] {5, 4}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(1, Kata.MatchArrays(new int[] {0, -1, 1, 4}, new int[] {-1}));
    }
}