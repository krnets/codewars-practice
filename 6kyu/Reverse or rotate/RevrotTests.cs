using System;
using NUnit.Framework;

[TestFixture]
public static class RevrotTests
{
    private static void Testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Testing(Revrot.RevRot("1234", 0), "");
    }

    [Test]
    public static void Test2()
    {
        Testing(Revrot.RevRot("", 0), "");
    }

    [Test]
    public static void Test3()
    {
        Testing(Revrot.RevRot("1234", 5), "");
    }

    [Test]
    public static void Test4()
    {
        String s = "733049910872815764";
        Testing(Revrot.RevRot(s, 5), "330479108928157");
    }

    [Test]
    public static void Test6()
    {
        String s = "73304991087281576455176044327690580265896";
        Testing(Revrot.RevRot(s, 8), "1994033775182780067155464327690480265895");
    }

    [Test]
    public static void Test7()
    {
        String s = "73304991087281576455176044327690580265896896028";
        Testing(Revrot.RevRot(s, 8), "1994033775182780067155464327690480265895");
    }

    [Test]
    public static void Test8()
    {
        String s = "73304991087281576455176044327690580265896896028126182265439";
        Testing(Revrot.RevRot(s, 11), "3304991087781576455172509672344060265896896862281621820");
    }

    [Test]
    public static void Test9()
    {
        String s = "73304991087281576455176044327690580265896896028126182265439441215340989";
        Testing(Revrot.RevRot(s, 14), "1827801994033776455176044325690580265896875622816218206939441215340984");
    }

    [Test]
    public static void Test10()
    {
        String s = "563000655734469485";
        Testing(Revrot.RevRot(s, 4), "0365065073456944");
    }

    [Test]
    public static void Test11()
    {
        String s = "56300065573446948588855";
        Testing(Revrot.RevRot(s, 3), "365000556437694854888");
    }

    [Test]
    public static void Test12()
    {
        String s = "56300065573446948588855200928875449742090";
        Testing(Revrot.RevRot(s, 6), "000365437556584964255888092880794457");
    }

    [Test]
    public static void Test13()
    {
        String s = "56300065573446948588855200928875449742090827299285754137212";
        Testing(Revrot.RevRot(s, 11), "3755600036546948588854457882900257280902479499285754132");
    }

    [Test]
    public static void Test14()
    {
        String s = "56300065573446948588855200928875449742090827299285754137212673841954794395427";
        Testing(Revrot.RevRot(s, 10), "6300065575446948588355200928885449742097582992728062127314573841954797");
    }
}