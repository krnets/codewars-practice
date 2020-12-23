using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.That(Kata.ExpandedForm(12), Is.EqualTo("10 + 2"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.That(Kata.ExpandedForm(42), Is.EqualTo("40 + 2"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.That(Kata.ExpandedForm(70304), Is.EqualTo("70000 + 300 + 4"));
    }
}