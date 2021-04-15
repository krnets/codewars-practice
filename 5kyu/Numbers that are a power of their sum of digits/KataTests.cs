using NUnit.Framework;

[TestFixture]
public static class PowerSumDigTests
{
    private static void testing(long actual, long expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        testing(PowerSumDig.PowerSumDigTerm(1), 81);
    }

    [Test]
    public static void Test2()
    {
        testing(PowerSumDig.PowerSumDigTerm(2), 512);
    }

    [Test]
    public static void Test3()
    {
        testing(PowerSumDig.PowerSumDigTerm(3), 2401);
    }

    [Test]
    public static void Test4()
    {
        testing(PowerSumDig.PowerSumDigTerm(4), 4913);
    }
}