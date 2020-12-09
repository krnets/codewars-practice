using NUnit.Framework;

[TestFixture]
public class KataOpenOrSeniorTests
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(new[] {"Open", "Senior", "Open", "Senior"},
            Kata.OpenOrSenior(new[] {new[] {45, 12}, new[] {55, 21}, new[] {19, 2}, new[] {104, 20}}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(new[] {"Open", "Open", "Open", "Open"},
            Kata.OpenOrSenior(new[] {new[] {3, 12}, new[] {55, 1}, new[] {91, -2}, new[] {54, 23}}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(new[] {"Senior", "Open", "Open", "Open"},
            Kata.OpenOrSenior(new[] {new[] {59, 12}, new[] {45, 21}, new[] {-12, -2}, new[] {12, 12}}));
    }
}