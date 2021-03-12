using System;
using NUnit.Framework;

[TestFixture]
public static class PentanacciTests
{
    private static void testing(long actual, long expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Console.WriteLine("Fixed Tests: CountOddPentaFib, low values");
        long[] lstI = new long[] {45, 68, 76, 100, 121};
        long[] resultsI = new long[] {15, 23, 25, 33, 40};
        for (int i = 0; i <= 4; i++)
        {
            testing(Pentanacci.CountOddPentaFib(lstI[i]), resultsI[i]);
        }
    }

    [Test]
    public static void Test2()
    {
        Console.WriteLine("Fixed Tests: CountOddPentaFib, moderate values");
        long[] lstII = new long[] {1508, 2100, 3500, 4200, 7600, 8555, 9100, 9999};
        long[] resultsII = new long[] {503, 699, 1167, 1399, 2533, 2851, 3033, 3333};
        for (int i = 0; i <= 7; i++)
        {
            testing(Pentanacci.CountOddPentaFib(lstII[i]), resultsII[i]);
        }
    }

    [Test]
    public static void Test3()
    {
        Console.WriteLine("Fixed Tests: CountOddPentaFib, moderate values");
        long[] lstIII = new long[] {13000, 15000, 16500, 17000, 18500, 20000, 25000, 32000, 34000, 37000, 40000, 44000};
        long[] resultsIII = new long[] {4333, 4999, 5499, 5667, 6167, 6667, 8333, 10667, 11333, 12333, 13333, 14667};
        for (int i = 0; i <= 11; i++)
        {
            testing(Pentanacci.CountOddPentaFib(lstIII[i]), resultsIII[i]);
        }
    }
}