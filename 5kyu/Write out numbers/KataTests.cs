using NUnit.Framework;

[TestFixture]
public class Number2WordsTests
{
    [Test]
    public void Test0()
    {
        Assert.AreEqual("zero", NumberTranslation.Number2Words(0));
    }

    [Test]
    public void Test1()
    {
        Assert.AreEqual("one", NumberTranslation.Number2Words(1));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual("three", NumberTranslation.Number2Words(3));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual("five", NumberTranslation.Number2Words(5));
    }

    [Test]
    public void Test8()
    {
        Assert.AreEqual("eight", NumberTranslation.Number2Words(8));
    }

    [Test]
    public void Test20()
    {
        Assert.AreEqual("twenty", NumberTranslation.Number2Words(20));
    }

    [Test]
    public void Test301()
    {
        Assert.AreEqual("three hundred one", NumberTranslation.Number2Words(301));
    }

    [Test]
    public void Test793()
    {
        Assert.AreEqual("seven hundred ninety-three", NumberTranslation.Number2Words(793));
    }

    [Test]
    public void Test800()
    {
        Assert.AreEqual("eight hundred", NumberTranslation.Number2Words(800));
    }

    [Test]
    public void Test650()
    {
        Assert.AreEqual("six hundred fifty", NumberTranslation.Number2Words(650));
    }

    [Test]
    public void Test1000()
    {
        Assert.AreEqual("one thousand", NumberTranslation.Number2Words(1000));
    }

    [Test]
    public void Test1003()
    {
        Assert.AreEqual("one thousand three", NumberTranslation.Number2Words(1003));
    }

    [Test]
    public void Test42553()
    {
        Assert.AreEqual("forty-two thousand five hundred fifty-three", NumberTranslation.Number2Words(42553));
    }

    [Test]
    public void Test513906()
    {
        Assert.AreEqual("five hundred thirteen thousand nine hundred six", NumberTranslation.Number2Words(513906));
    }

    [Test]
    public void Test628393()
    {
        Assert.AreEqual("six hundred twenty-eight thousand three hundred ninety-three",
            NumberTranslation.Number2Words(628393));
    }
}