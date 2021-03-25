using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void EncodeTests()
    {
        Assert.AreEqual("Ala has a cat", Kata.Encode("Gug hgs g cgt", "gaderypoluki"));
        Assert.AreEqual("Dance on the table", Kata.Encode("Dkucr pu yhr ykbir", "politykarenu"));
    }

    [Test]
    public void DecodeTests()
    {
        Assert.AreEqual("gaderypoluki", Kata.Decode("agedyropulik", "gaderypoluki"));
        Assert.AreEqual("Hide our beers", Kata.Decode("Hmdr nge brres", "regulaminowy"));
    }
}