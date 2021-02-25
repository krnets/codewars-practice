using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("The Knife", Kata.BandNameGenerator("knife"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("Tartart", Kata.BandNameGenerator("tart"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("Sandlesandles", Kata.BandNameGenerator("sandles"));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual("The Bed", Kata.BandNameGenerator("bed"));
    }
}