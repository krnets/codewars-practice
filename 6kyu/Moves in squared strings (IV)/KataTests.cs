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
    public static void TestRot90Counter()
    {
        Console.WriteLine("Fixed Tests Rot90Counter");
        testing(Opstrings.Oper(Opstrings.Rot90Counter, "EcGcXJ\naaygcA\nNgIshN\nyOrCZE\neBEqpm\nNkxCgw"),
            "JANEmw\nXchZpg\ncgsCqC\nGyIrEx\ncagOBk\nEaNyeN");
    }

    [Test]
    public static void TestDiag2Sym()
    {
        Console.WriteLine("Fixed Tests Diag2Sym");
        // testing(Opstrings.Oper(Opstrings.Diag2Sym, "LmvLyg\nDKELBm\nylJhui\nXRXqHD\nzlisCT\nhPqxYb"),
        //     "bTDimg\nYCHuBy\nxsqhLL\nqiXJEv\nPlRlKm\nhzXyDL");
        testing(Opstrings.Oper(Opstrings.Diag2Sym, "abcd\nefgh\nijkl\nmnop"), "plhd\nokgc\nnjfb\nmiea");
    }

    [Test]
    public static void TestSelfieDiag2Counterclock()
    {
        Console.WriteLine("Fixed Tests SelfieDiag2Counterclock");
        testing(Opstrings.Oper(Opstrings.SelfieDiag2Counterclock, "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg"),
            "NJVGhr|gKilwr|rwliKg\nMObsvw|WLhtvh|hvthLW\ntPhCtl|iRnCsG|GsCnRi\nsoEnhi|lQEhbV|VbhEQl\nrtQRLK|jtoPOJ|JOPotj\nzjliWg|zrstMN|NMtsrz");
    }
}