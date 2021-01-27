using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("", Kata.GenerateShape(0));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("+", Kata.GenerateShape(1));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("++\n++", Kata.GenerateShape(2));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual("+++\n+++\n+++", Kata.GenerateShape(3));
    }
}