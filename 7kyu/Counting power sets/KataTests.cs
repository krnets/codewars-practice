using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(1, Kata.Powers(new int[] { }));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(2, Kata.Powers(new int[] {1}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(4, Kata.Powers(new int[] {1, 2}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(16, Kata.Powers(new int[] {1, 2, 3, 4}));
    }
}