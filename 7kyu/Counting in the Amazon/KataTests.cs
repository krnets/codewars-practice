using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.AreEqual("anane", Kata.CountArara(1));
        Assert.AreEqual("adak anane", Kata.CountArara(3));
        Assert.AreEqual("adak adak adak adak", Kata.CountArara(8));
    }
}