using System;
using System.Linq;
using NUnit.Framework;

[TestFixture]
public static class OpstringsTests
{
    private static void testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void TestVertical1()
    {
        testing(Opstrings.Oper(Opstrings.VertMirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"),
            "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw");
    }

    [Test]
    public static void TestVertical2()
    {
        testing(Opstrings.Oper(Opstrings.VertMirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"),
            "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP");
    }

    [Test]
    public static void TestHotMirror1()
    {
        testing(Opstrings.Oper(Opstrings.HorMirror, "lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt");
    }

    [Test]
    public static void TestHotMirror2()
    {
        testing(Opstrings.Oper(Opstrings.HorMirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK");
    }
}