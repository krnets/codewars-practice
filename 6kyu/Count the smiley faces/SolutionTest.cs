using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(4, Kata.CountSmileys(new[] {":D", ":~)", ";~D", ":)"}));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(2, Kata.CountSmileys(new[] {":)", ":(", ":D", ":O", ":;"}));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(1, Kata.CountSmileys(new[] {";]", ":[", ";*", ":$", ";-D"}));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(0, Kata.CountSmileys(new[] {";", ")", ";*", ":$", "8-D"}));
    }
}