using NUnit.Framework;

[TestFixture]
public static class StepInPrimesTests
{
    [Test]
    public static void Test1()
    {
        Assert.AreEqual(new long[] {101, 103}, StepInPrimes.Step(2, 100, 110));
    }

    [Test]
    public static void Test2()
    {
        Assert.AreEqual(new long[] {103, 107}, StepInPrimes.Step(4, 100, 110));
    }

    [Test]
    public static void Test3()
    {
        Assert.AreEqual(new long[] {101, 107}, StepInPrimes.Step(6, 100, 110));
    }

    [Test]
    public static void Test4()
    {
        Assert.AreEqual(new long[] {359, 367}, StepInPrimes.Step(8, 300, 400));
    }

    [Test]
    public static void Test5()
    {
        Assert.AreEqual(new long[] {307, 317}, StepInPrimes.Step(10, 300, 400));
    }

    [Test]
    public static void Test6()
    {
        Assert.AreEqual(null, StepInPrimes.Step(11, 30000, 100000));
    }
}