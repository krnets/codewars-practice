using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.That(Kata.GolfScoreCalculator("453454444344544443", "354445334534445348"), Is.EqualTo(3));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.That(Kata.GolfScoreCalculator("333333333333333333", "444444444444444444"), Is.EqualTo(18));
    }
}