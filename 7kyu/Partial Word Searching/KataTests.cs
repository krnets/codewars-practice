using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
        {
        Assert.AreEqual(new string[] {"ab", "abc", "zab"},
            Kata.WordSearch("ab", new string[] {"za", "ab", "abc", "zab", "zbc"}));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new string[] {"ab", "abc", "zab"},
            Kata.WordSearch("aB", new string[] {"za", "ab", "abc", "zab", "zbc"}));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(new string[] {"aB", "Abc", "zAB"},
            Kata.WordSearch("ab", new string[] {"za", "aB", "Abc", "zAB", "zbc"}));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(new string[] {"Empty"},
            Kata.WordSearch("abcd", new string[] {"za", "aB", "Abc", "zAB", "zbc"}));
    }
}