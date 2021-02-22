using System;
using System.Numerics;
using NUnit.Framework;

[TestFixture]
public static class HiddenSeqTests
{
    private static void testing(BigInteger actual, BigInteger expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Console.WriteLine("Testing fcn");
        testing(HiddenSeq.fcn(17), new BigInteger(131072));
        testing(HiddenSeq.fcn(21), new BigInteger(2097152));
        testing(HiddenSeq.fcn(14), new BigInteger(16384));
        testing(HiddenSeq.fcn(43), new BigInteger(8796093022208L));
        testing(HiddenSeq.fcn(19), new BigInteger(524288));
    }
}