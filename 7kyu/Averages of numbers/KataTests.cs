using NUnit.Framework;

public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(string.Join(", ", new double[] {2, 2, 2, 2}),
            string.Join(", ", Kata.Averages(new int[] {2, 2, 2, 2, 2})));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(string.Join(", ", new double[] {0, 0, 0, 0}),
            string.Join(", ", Kata.Averages(new int[] {2, -2, 2, -2, 2})));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(string.Join(", ", new double[] {2, 4, 3, -4.5}),
            string.Join(", ", Kata.Averages(new int[] {1, 3, 5, 1, -10})));
    }
}