using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void EncodeTests()
    {
        Assert.AreEqual("Gug hgs g cgt", Kata.Encode("Ala has a cat"));
        Assert.AreEqual("GBCE", Kata.Encode("ABCD"));
        Assert.AreEqual("Gug hgs g cgt", Kata.Encode("Ala has a cat"));
        Assert.AreEqual("agedyropulik", Kata.Encode("gaderypoluki"));
    }

    [Test]
    public void DecodeTests()
    {
        Assert.AreEqual("Ala has a cat", Kata.Decode("Gug hgs g cgt"));
        Assert.AreEqual("gaderypoluki", Kata.Decode("agedyropulik"));
        Assert.AreEqual("ABCD", Kata.Decode("GBCE"));
    }
}