using NUnit.Framework;

[TestFixture]
public static class BeforeAfterPrimesTests
{
    [Test]
    public static void Test97()
    {
        Assert.AreEqual(new int[] {89, 101}, BeforeAfterPrimes.PrimeBefAft(97));
    }

    [Test]
    public static void Test100()
    {
        Assert.AreEqual(new int[] {97, 101}, BeforeAfterPrimes.PrimeBefAft(100));
    }

    [Test]
    public static void Test101()
    {
        Assert.AreEqual(new int[] {97, 103}, BeforeAfterPrimes.PrimeBefAft(101));
    }
}