using System;
using NUnit.Framework;

[TestFixture]
public static class SumFractionsTests
{
    private static void testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void test()
    {
        int[,] a = {{1, 2}, {2, 9}, {3, 18}, {4, 24}, {6, 48}};
        String r = "[85, 72]";
        testing(SumFractions.SumFracts(a), r);
        a = new[,] {{1, 2}, {1, 3}, {1, 4}};
        r = "[13, 12]";
        testing(SumFractions.SumFracts(a), r);
        a = new[,] {{1, 3}, {5, 3}};
        r = "2";
        testing(SumFractions.SumFracts(a), r);
        a = new int[,] { };
        testing(SumFractions.SumFracts(a), null);
    }
}