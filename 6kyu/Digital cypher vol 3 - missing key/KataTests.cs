using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(1939, Kata.FindTheKey("scout", new int[] {20, 12, 18, 30, 21}));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(1939, Kata.FindTheKey("masterpiece", new int[] {14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8}));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(12, Kata.FindTheKey("nomoretears", new int[] {15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20}));
    }
}