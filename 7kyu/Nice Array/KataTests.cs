using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(true, Kata.IsNice(new int[] {2, 10, 9, 3}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(false, Kata.IsNice(new int[] {3, 4, 5, 7}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(false, Kata.IsNice(new int[] { }));
    }
}