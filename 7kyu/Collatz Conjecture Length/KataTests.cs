using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(8, Kata.Collatz(20));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(18, Kata.Collatz(15));
    }
}