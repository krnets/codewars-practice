using NUnit.Framework;
using System;
class ExampleTest
{
    [Test]
    public void FixedTest()
    {
        Assert.AreEqual("a", Kata.HasSubpattern("a"));
        Assert.AreEqual("a", Kata.HasSubpattern("aaaa"));
        Assert.AreEqual("abcd", Kata.HasSubpattern("abcd"));
        Assert.AreEqual("ab", Kata.HasSubpattern("babababababababa"));
        Assert.AreEqual("ab", Kata.HasSubpattern("bbabbaaabbaaaabb"));
        Assert.AreEqual("123a", Kata.HasSubpattern("123a123a123a"));
        Assert.AreEqual("111222333Aaa", Kata.HasSubpattern("123A123a123a"));
        Assert.AreEqual("123a", Kata.HasSubpattern("12aa13a21233"));
        Assert.AreEqual("111222333Aaaa", Kata.HasSubpattern("12aa13a21233A"));
        Assert.AreEqual("aaabbccccdd", Kata.HasSubpattern("abcdabcaccd"));
    }
}