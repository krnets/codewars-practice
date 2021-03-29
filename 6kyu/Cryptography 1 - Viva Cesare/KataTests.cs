using NUnit.Framework;

[TestFixture]
public class CaesarCryptoTest
{
    [Test]
    public void Encode_BasicTest()
    {
        Assert.AreEqual("Hw wx, Euxwh?", CaesarCrypto.Encode("Et tu, Brute?", 3));
    }

    [Test]
    public void Encode_BasicInverselyTest()
    {
        Assert.AreEqual("Et tu, Brute?", CaesarCrypto.Encode("Hw wx, Euxwh?", -3));
    }
}