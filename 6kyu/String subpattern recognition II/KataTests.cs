using NUnit.Framework;

class ExampleTest
{
    [Test]
    public void FixedTest()
    {
        Assert.AreEqual(false, Kata.HasSubpattern("a"));
        Assert.AreEqual(true, Kata.HasSubpattern("aaaa"));
        Assert.AreEqual(false, Kata.HasSubpattern("abcd"));
        Assert.AreEqual(true, Kata.HasSubpattern("babababababababa"));
        Assert.AreEqual(true, Kata.HasSubpattern("bbabbaaabbaaaabb"));
        Assert.AreEqual(true, Kata.HasSubpattern("123a123a123a"));
        Assert.AreEqual(false, Kata.HasSubpattern("123A123a123a"));
        Assert.AreEqual(true, Kata.HasSubpattern("12aa13a21233"));
        Assert.AreEqual(false, Kata.HasSubpattern("12aa13a21233A"));
        Assert.AreEqual(false, Kata.HasSubpattern("abcdabcaccd"));
    }
}