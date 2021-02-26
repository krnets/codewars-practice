using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("Safe!",
            Kata.StrongEnough(new int[][] {new int[] {2, 3, 1}, new int[] {3, 1, 1,}, new int[] {1, 1, 2}}, 2));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("Safe!",
            Kata.StrongEnough(new int[][] {new int[] {5, 8, 7}, new int[] {3, 3, 1,}, new int[] {4, 1, 2}}, 2));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("Needs Reinforcement!",
            Kata.StrongEnough(new int[][] {new int[] {5, 8, 7}, new int[] {3, 3, 1,}, new int[] {4, 1, 2}}, 3));
    }
}