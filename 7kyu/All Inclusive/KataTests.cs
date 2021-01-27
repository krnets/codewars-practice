using System;
using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public static class RotationsTests
{
    private static void testing(Boolean actual, Boolean expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        var a = new List<string> 
            {"bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"};
        testing(Rotations.ContainAllRots("bsjq", a), true);
    }

    [Test]
    public static void Test2()
    {
        var a = new List<string>();
        testing(Rotations.ContainAllRots("", a), true);
    }

    [Test]
    public static void Test3()
    {
        var a = new List<string> {"bsjq", "qbsj"};
        testing(Rotations.ContainAllRots("", a), true);
    }

    [Test]
    public static void Test4()
    {
        var a = new List<string> {"TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"};
        testing(Rotations.ContainAllRots("XjYABhR", a), false);
    }
}