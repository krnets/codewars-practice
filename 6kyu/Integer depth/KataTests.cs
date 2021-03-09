using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(10, Kata.ComputeDepth(1));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(9, Kata.ComputeDepth(42));
    }
}