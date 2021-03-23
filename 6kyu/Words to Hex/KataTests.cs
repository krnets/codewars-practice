using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(
            new[] {"#48656c", "#6d7900", "#6e616d", "#697300", "#476172", "#616e64", "#490000", "#6c696b", "#636865"},
            Kata.WordsToHex("Hello, my name is Gary and I like cheese."));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(new[] {"#303132"}, Kata.WordsToHex("0123456789"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(new[] {"#546869"}, Kata.WordsToHex("ThisIsOneLongSentenceThatConsistsOfWords"));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(new[] {"#426c61", "#626c61", "#626c61", "#626c61"},
            Kata.WordsToHex("Blah blah blah blaaaaaaaaaaaah"));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual(new[] {"#262626", "#242424", "#5e5e5e", "#404040", "#282928"},
            Kata.WordsToHex("&&&&& $$$$$ ^^^^^ @@@@@ ()()()()("));
    }
}