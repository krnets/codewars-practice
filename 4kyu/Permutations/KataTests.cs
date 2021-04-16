using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;

public class SolutionTest
{
    [Test]
    public void Example0()
    {
        Assert.AreEqual(new List<string> {string.Empty}, Permutations.SinglePermutations(string.Empty).OrderBy(x => x).ToList());
    }

    [Test]
    public void Example1()
    {
        Assert.AreEqual(new List<string> {"a"}, Permutations.SinglePermutations("a").OrderBy(x => x).ToList());
    }

    [Test]
    public void Example2()
    {
        Assert.AreEqual(new List<string> {"ab", "ba"}, Permutations.SinglePermutations("ab").OrderBy(x => x).ToList());
    }

    [Test]
    public void Example3()
    {
        Assert.AreEqual(new List<string> {"aabb", "abab", "abba", "baab", "baba", "bbaa"},
            Permutations.SinglePermutations("aabb").OrderBy(x => x).ToList());
    }

    [Test]
    public void UniqueLetters()
    {
        var abcd = new List<string>
        {
            "abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad", "bcda", "bdac", "bdca",
            "cabd", "cadb", "cbad", "cbda", "cdab", "cdba", "dabc", "dacb", "dbac", "dbca", "dcab", "dcba"
        };

        Assert.AreEqual(abcd, Permutations.SinglePermutations("abcd").OrderBy(x => x).ToList());
        Assert.AreEqual(abcd, Permutations.SinglePermutations("bcad").OrderBy(x => x).ToList());
        Assert.AreEqual(abcd, Permutations.SinglePermutations("dcba").OrderBy(x => x).ToList());
    }

    [Test]
    public void DuplicateLetters()
    {
        Assert.AreEqual(new List<string> {"aa"}, Permutations.SinglePermutations("aa").OrderBy(x => x).ToList());
        Assert.AreEqual(new List<string> {"aaaab", "aaaba", "aabaa", "abaaa", "baaaa"},
            Permutations.SinglePermutations("aaaab").OrderBy(x => x).ToList());
        Assert.AreEqual(new List<string> {"aaaaab", "aaaaba", "aaabaa", "aabaaa", "abaaaa", "baaaaa"},
            Permutations.SinglePermutations("aaaaab").OrderBy(x => x).ToList());
    }
}