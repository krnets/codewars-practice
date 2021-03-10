using System;
using NUnit.Framework;

[TestFixture]
public static class DecodingTests
{
    public static void testing_decode(String r, String expected)
    {
        String actual = Decoding.Decode(r);
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        testing_decode("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx");
    }

    [Test]
    public static void Test2()
    {
        testing_decode("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb");
    }

    [Test]
    public static void Test3()
    {
        testing_decode("105860ymmgegeeiwaigsqkcaeguicc", "Impossible to decode");
    }
}