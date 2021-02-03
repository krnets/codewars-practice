using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.That(Kata.Solve("xyab", "xzca"), Is.EqualTo("ybzc"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.That(Kata.Solve("xyabb", "xzca"), Is.EqualTo("ybbzc"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.That(Kata.Solve("abcd", "xyz"), Is.EqualTo("abcdxyz"));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.That(Kata.Solve("xxx", "xzca"), Is.EqualTo("zca"));
    }
}