using NUnit.Framework;

class ExampleTest
{
    [Test]
    public void FixedTest()
    {
        Assert.AreEqual(false, Kata.HasSubpattern("a"));
        Assert.AreEqual(true, Kata.HasSubpattern("aaaa"));
        Assert.AreEqual(false, Kata.HasSubpattern("abcd"));
        Assert.AreEqual(true, Kata.HasSubpattern("abababab"));
        Assert.AreEqual(false, Kata.HasSubpattern("ababababa"));
        Assert.AreEqual(true, Kata.HasSubpattern("123a123a123a"));
        Assert.AreEqual(false, Kata.HasSubpattern("123A123a123a"));
        Assert.AreEqual(true, Kata.HasSubpattern("abbaabbaabba"));
        Assert.AreEqual(false, Kata.HasSubpattern("abbabbabba"));
        Assert.AreEqual(false, Kata.HasSubpattern("abcdabcabcd"));
    }
}