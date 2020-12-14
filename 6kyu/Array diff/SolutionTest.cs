using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(new int[] {2}, Kata.ArrayDiff(new int[] {1, 2}, new int[] {1}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(new int[] {2, 2}, Kata.ArrayDiff(new int[] {1, 2, 2}, new int[] {1}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(new int[] {1}, Kata.ArrayDiff(new int[] {1, 2, 2}, new int[] {2}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(new int[] {1, 2, 2}, Kata.ArrayDiff(new int[] {1, 2, 2}, new int[] { }));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual(new int[] { }, Kata.ArrayDiff(new int[] { }, new int[] {1, 2}));
    }
}