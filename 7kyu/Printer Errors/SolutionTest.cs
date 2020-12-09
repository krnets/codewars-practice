using System;
using NUnit.Framework;

[TestFixture]
public static class PrinterTests
{
    private static Random rnd = new Random();

    [Test]
    public static void test1()
    {
        Console.WriteLine("Testing PrinterError");
        string s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
        Assert.AreEqual("3/56", Printer.PrinterError(s));
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
        Assert.AreEqual("6/60", Printer.PrinterError(s));
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu";
        Assert.AreEqual("11/65", Printer.PrinterError(s));
    }
}