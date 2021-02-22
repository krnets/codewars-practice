using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("10", Kata.EvensAndOdds(2));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("d", Kata.EvensAndOdds(13));
    }
}