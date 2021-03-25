using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual("-", Kata.ReplaceAll("", "", "-"), "Empty input, empty find");
        Assert.AreEqual("-1-", Kata.ReplaceAll("1", "", "-"), "Single-character input, empty find");
        Assert.AreEqual("-1-2-3-", Kata.ReplaceAll("123", "", "-"), "Empty string as find");
        Assert.AreEqual("string", Kata.ReplaceAll("string", "find", "replace"), "No matches found");
        Assert.AreEqual("str!-str!", Kata.ReplaceAll("string-string", "ing", "!"), "Matches found");
        Assert.AreEqual("string", Kata.ReplaceAll("", "", "string"), "Empty string as find");
        Assert.AreEqual("-s-t-r-i-n-g-", Kata.ReplaceAll("string", "", "-"), "Empty string as find");
        Assert.AreEqual("replaced", Kata.ReplaceAll("string", "string", "replaced"), "Original string as find");
        Assert.AreEqual("sg", Kata.ReplaceAll("string", "trin", ""), "Replace with empty string");
        Assert.AreEqual("ss", Kata.ReplaceAll("s", "s", "ss"), "Replace has find string included");
        Assert.AreEqual("123-", Kata.ReplaceAll("123\\^$.|?*+()[]{}", "\\^$.|?*+()[]{}", "-"),
            "$ replaced (regex gotcha)");
    }
}