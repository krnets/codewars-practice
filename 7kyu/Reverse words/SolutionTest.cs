using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void Example()
    {
        Assert.AreEqual("sihT si na !elpmaxe", Kata.ReverseWords("This is an example!"));
    }

    [Test]
    public void QuickBrownFox()
    {
        Assert.AreEqual("ehT kciuq nworb xof spmuj revo eht yzal .god",
            Kata.ReverseWords("The quick brown fox jumps over the lazy dog."));
    }

    [Test]
    public void OneWord()
    {
        Assert.AreEqual("elppa", Kata.ReverseWords("apple"));
    }

    [Test]
    public void DoubleSpaces()
    {
        Assert.AreEqual("elbuod  decaps  sdrow", Kata.ReverseWords("double  spaced  words"));
    }
}