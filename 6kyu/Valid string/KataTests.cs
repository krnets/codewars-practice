using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [TestCase(new[] {"code", "wars"}, "codewars", true)]
    [TestCase(new[] {"code", "wars"}, "codewar", false)]
    [TestCase(new[] {"wars", "code"}, "codewars", true)]
    [TestCase(new[] {"code", "wars"}, "codecodewars", true)]
    [TestCase(new[] {"code", "wars"}, "codewarscode", true)]
    [TestCase(new[] {"code", "star", "wars"}, "starwars", true)]
    [TestCase(new[] {"Star", "Code", "Wars"}, "StarCodeWars", true)]
    [TestCase(new[] {"Star", "Code", "Wars"}, "WarsStarCode", true)]
    [TestCase(new[] {"Star", "Code", "Wars"}, "CodeStarsWar", false)]
    [TestCase(new string[] { }, "codewars", false)]
    [TestCase(new[] {"code", "wars"}, "code", true)]
    [TestCase(new[] {"a", "b", "c", "d", "e", "f"}, "abcdef", true)]
    [TestCase(new[] {"a", "b", "c", "d", "e", "f"}, "abcdefg", false)]
    [TestCase(new string[] {"ab", "a", "bc"}, "abc", true)]
    [TestCase(new string[] {"ab", "bc"}, "abc", false)]
    public void FixedTest(string[] dictionary, string word, bool expected)
    {
        Assert.AreEqual(expected, Kata.ValidateString(dictionary, word));
    }
}