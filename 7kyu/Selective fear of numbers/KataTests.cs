using NUnit.Framework;

[TestFixture]
public class AmIAfraidTests
{
    [Test]
    public static void TestFixed()
    {
        Assert.AreEqual(false, Kata.AmIAfraid("Monday", 13));
        Assert.AreEqual(true, Kata.AmIAfraid("Sunday", -666));
        Assert.AreEqual(false, Kata.AmIAfraid("Tuesday", 2));
        Assert.AreEqual(true, Kata.AmIAfraid("Tuesday", 965));
        Assert.AreEqual(true, Kata.AmIAfraid("Friday", 2));
    }
}