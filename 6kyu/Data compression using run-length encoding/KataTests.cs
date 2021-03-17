using NUnit.Framework;

[TestFixture]
public class RleCompressionTests
{
    [TestCase("A", "1A")]
    [TestCase("AAA", "3A")]
    [TestCase("AB", "1A1B")]
    [TestCase("AAABBBCCCA", "3A3B3C1A")]
    public void TestEncode(string input, string expectedOutput)
    {
        var output = new RleCompression().Encode(input);
        Assert.AreEqual(expectedOutput, output);
    }

    [TestCase("1A", "A")]
    [TestCase("3A", "AAA")]
    [TestCase("1A1B", "AB")]
    [TestCase("3A3B3C1A", "AAABBBCCCA")]
    public void TestDecode(string input, string expectedOutput)
    {
        var output = new RleCompression().Decode(input);
        Assert.AreEqual(expectedOutput, output);
    }

    [TestCase("AAAAAAAAAAB")]
    [TestCase("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
    public void TestRoundTrip(string str)
    {
        var comp = new RleCompression();
        var encoded = comp.Encode(str);
        var decoded = comp.Decode(encoded);

        Assert.AreEqual(str, decoded);
    }
}