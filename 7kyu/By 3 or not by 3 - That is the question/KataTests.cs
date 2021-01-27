using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.That(Kata.DivisibleByThree("1891009"), Is.EqualTo(false));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.That(Kata.DivisibleByThree("00009"), Is.EqualTo(true));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.That(Kata.DivisibleByThree("57"), Is.EqualTo(true));
    }
}