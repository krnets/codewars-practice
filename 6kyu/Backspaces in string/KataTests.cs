using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("ac", Kata.CleanString("abc#d##c"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("", Kata.CleanString("abc####d##c#"));
    }
}