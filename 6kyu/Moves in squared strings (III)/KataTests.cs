using System;
using NUnit.Framework;

[TestFixture]
public static class OpstringsTests
{
    private static void testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void TestRot90Clock()
    {
        Console.WriteLine("Fixed Tests Rot90Clock");
        testing(Opstrings.Oper(Opstrings.Rot90Clock, "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb"),
            "Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle");

        testing(Opstrings.Oper(Opstrings.Rot90Clock, "abcd\nefgh\nijkl\nmnop"), "miea\nnjfb\nokgc\nplhd");
    }

    [Test]
    public static void TestDiag1Sym()
    {
        Console.WriteLine("Fixed Tests Diag1Sym");
        testing(Opstrings.Oper(Opstrings.Diag1Sym, "wuUyPC\neNHWxw\nehifmi\ntBTlFI\nvWNpdv\nIFkGjZ"),
            "weetvI\nuNhBWF\nUHiTNk\nyWflpG\nPxmFdj\nCwiIvZ");

        testing(Opstrings.Oper(Opstrings.Diag1Sym, "abcd\nefgh\nijkl\nmnop"), "aeim\nbfjn\ncgko\ndhlp");
    }

    [Test]
    public static void TestSelfieAndDiag1()
    {
        Console.WriteLine("Fixed Tests SelfieAndDiag1");
        testing(Opstrings.Oper(Opstrings.SelfieAndDiag1, "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg"),
            "NJVGhr|NMtsrz\nMObsvw|JOPotj\ntPhCtl|VbhEQl\nsoEnhi|GsCnRi\nrtQRLK|hvthLW\nzjliWg|rwliKg");
    }
}