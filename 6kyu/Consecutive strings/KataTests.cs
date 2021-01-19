using System;
using NUnit.Framework;

[TestFixture]
public static class LongestConsecutivesTests
{
    private static void testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void test1()
    {
        testing(
            LongestConsecutives.LongestConsec(
                new String[] {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"}, 2),
            "abigailtheta");
    }

    [Test]
    public static void test2()
    {
        testing(
            LongestConsecutives.LongestConsec(
                new String[] {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"}, 1),
            "oocccffuucccjjjkkkjyyyeehh");
    }

    [Test]
    public static void test3()
    {
        testing(LongestConsecutives.LongestConsec(new String[] { }, 3), "");
    }

    [Test]
    public static void test4()
    {
        testing(
            LongestConsecutives.LongestConsec(
                new String[] {"itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"},
                2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck");
    }

    [Test]
    public static void test5()
    {
        testing(
            LongestConsecutives.LongestConsec(new String[] {"wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"}, 2),
            "wlwsasphmxxowiaxujylentrklctozmymu");
    }

    [Test]
    public static void test6()
    {
        testing(LongestConsecutives.LongestConsec(new String[] {"zone", "abigail", "theta", "form", "libe", "zas"}, -2),
            "");
    }

    [Test]
    public static void test7()
    {
        testing(LongestConsecutives.LongestConsec(new String[] {"it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"}, 3),
            "ixoyx3452zzzzzzzzzzzz");
    }

    [Test]
    public static void test8()
    {
        testing(LongestConsecutives.LongestConsec(new String[] {"it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"}, 15),
            "");
    }

    [Test]
    public static void test9()
    {
        testing(LongestConsecutives.LongestConsec(new String[] {"it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"}, 0),
            "");
    }
}