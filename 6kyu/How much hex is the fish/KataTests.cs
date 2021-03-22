using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(1, Kata.FisHex("pufferfish"));
        Assert.AreEqual(14, Kata.FisHex("puffers"));
        Assert.AreEqual(14, Kata.FisHex("balloonfish"));
        Assert.AreEqual(4, Kata.FisHex("blowfish"));
        Assert.AreEqual(10, Kata.FisHex("bubblefish"));
        Assert.AreEqual(10, Kata.FisHex("globefish"));
        Assert.AreEqual(1, Kata.FisHex("swellfish"));
        Assert.AreEqual(8, Kata.FisHex("toadfish"));
        Assert.AreEqual(9, Kata.FisHex("toadies"));
        Assert.AreEqual(9, Kata.FisHex("honey toads"));
        Assert.AreEqual(13, Kata.FisHex("sugar toads"));
        Assert.AreEqual(5, Kata.FisHex("sea squab"));
    }
}