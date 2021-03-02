using System;
using NUnit.Framework;

[TestFixture]
public static class OperarrayTests
{
    private static void testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    public static string Array2String(long[] list)
    {
        return "[" + string.Join(",", list) + "]";
    }

    [Test]
    public static void Test0()
    {
        Console.WriteLine("Fixed Tests ; gcdi, lcmu, som, mini, maxi");
        long[] a = new long[] {18, 69, -90, -78, 65, 40};
        long[] r = new long[] {18, 3, 3, 3, 1, 1};
        long[] op = Operarray.OperArray(Operarray.gcdi, a, a[0]);
        testing(OperarrayTests.Array2String(op), OperarrayTests.Array2String(r));
        r = new long[] {18, 414, 2070, 26910, 26910, 107640};
        op = Operarray.OperArray(Operarray.lcmu, a, a[0]);
        testing(OperarrayTests.Array2String(op), OperarrayTests.Array2String(r));
        r = new long[] {18, 87, -3, -81, -16, 24};
        op = Operarray.OperArray(Operarray.som, a, 0);
        testing(OperarrayTests.Array2String(op), OperarrayTests.Array2String(r));
        r = new long[] {18, 18, -90, -90, -90, -90};
        op = Operarray.OperArray(Operarray.mini, a, a[0]);
        testing(OperarrayTests.Array2String(op), OperarrayTests.Array2String(r));
        r = new long[] {18, 69, 69, 69, 69, 69};
        op = Operarray.OperArray(Operarray.maxi, a, a[0]);
        testing(OperarrayTests.Array2String(op), OperarrayTests.Array2String(r));
    }
}