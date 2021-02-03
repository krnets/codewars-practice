using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest0()
    {
        Assert.AreEqual("", Kata.Babel(0));
    }

    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("o\n" +
                        "o\n" +
                        "o", Kata.Babel(1));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(" o\n" +
                        " o\n" +
                        " o\n" +
                        "ooo\n" +
                        "ooo\n" +
                        "ooo", Kata.Babel(2));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("  o\n" +
                        "  o\n" +
                        "  o\n" +
                        " ooo\n" +
                        " ooo\n" +
                        " ooo\n" +
                        "ooooo\n" +
                        "ooooo\n" +
                        "ooooo", Kata.Babel(3));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual("   o\n" +
                        "   o\n" +
                        "   o\n" +
                        "  ooo\n" +
                        "  ooo\n" +
                        "  ooo\n" +
                        " ooooo\n" +
                        " ooooo\n" +
                        " ooooo\n" +
                        "ooooooo\n" +
                        "ooooooo\n" +
                        "ooooooo", Kata.Babel(4));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual("    o\n" +
                        "    o\n" +
                        "    o\n" +
                        "   ooo\n" +
                        "   ooo\n" +
                        "   ooo\n" +
                        "  ooooo\n" +
                        "  ooooo\n" +
                        "  ooooo\n" +
                        " ooooooo\n" +
                        " ooooooo\n" +
                        " ooooooo\n" +
                        "ooooooooo\n" +
                        "ooooooooo\n" +
                        "ooooooooo", Kata.Babel(5));
    }
}