using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.That(Kata.Encrypt("", 1), Is.EqualTo(""));
        Assert.That(Kata.Encrypt("a", 1), Is.EqualTo("b"));
        Assert.That(Kata.Encrypt("please encrypt me", 2), Is.EqualTo("rngcug\"gpet{rv\"og"));
    }
}