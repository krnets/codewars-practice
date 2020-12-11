using NUnit.Framework;

[TestFixture]
public static class MaxDiffLengthTests
{
    [Test]
    public static void Test1()
    {
        string[] s1 =
        {
            "hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii",
            "dvvvwz"
        };
        string[] s2 = {"cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"};
        Assert.AreEqual(13, MaxDiffLength.Mxdiflg(s1, s2)); // 13
    }

    [Test]
    public static void Test2()
    {
        string[] s1 =
        {
            "ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"
        };

        string[] s2 =
        {
            "bbbaaayddqbbrrrv"
        };

        Assert.AreEqual(10, MaxDiffLength.Mxdiflg(s1, s2)); // 10
    }

    [Test]
    public static void Test3()
    {
        string[] s1 =
        {
            "ccct", "tkkeeeyy", "ggiikffsszzoo", "nnngssddu", "rrllccqqqqwuuurdd", "kkbbddaakkk"
        };

        string[] s2 =
        {
            "tttxxxxxxgiiyyy", "ooorcvvj", "yzzzhhhfffaaavvvpp", "jjvvvqqllgaaannn", "tttooo", "qmmzzbhhbb"
        };

        Assert.AreEqual(14, MaxDiffLength.Mxdiflg(s1, s2)); // 14  
    }

    [Test]
    public static void Test4()
    {
        string[] s1 =
        {
        };
        string[] s2 =
        {
            "bbbaaayddqbbrrrv"
        };

        Assert.AreEqual(-1, MaxDiffLength.Mxdiflg(s1, s2));
    }

    [Test]
    public static void Test5()
    {
        string[] s1 =
        {
            "ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"
        };

        string[] s2 =
        {
        };
        Assert.AreEqual(-1, MaxDiffLength.Mxdiflg(s1, s2));
    }

    [Test]
    public static void Test6()
    {
        string[] s1 =
        {
        };
        string[] s2 =
        {
        };
        Assert.AreEqual(-1, MaxDiffLength.Mxdiflg(s1, s2));
    }
}