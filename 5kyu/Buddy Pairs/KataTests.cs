using NUnit.Framework;
using System;

[TestFixture]
public class BudTest
{
    private static void testing(long start, long limit, string expected)
    {
        Console.WriteLine("start: {0}, limit: {1}, expected: {2}", start, limit, expected);
        Assert.AreEqual(expected, Bud.Buddy(start, limit));
    }

    [Test]
    public static void Test1()
    {
        testing(1071625, 1103735, "(1081184 1331967)");
    }

    [Test]
    public static void Test2()
    {
        testing(2382, 3679, "Nothing");
    }

    [Test]
    public static void Test3()
    {
        testing(8983, 13355, "(9504 20735)");
    }
}