using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void BasicTes1()
    {
        Assert.AreEqual("scout", Kata.Decode(new int[] {20, 12, 18, 30, 21}, 1939));
    }

    [Test]
    public void BasicTes2()
    {
        Assert.AreEqual("masterpiece", Kata.Decode(new int[] {14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8}, 1939));
    }
}