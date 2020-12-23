using NUnit.Framework;

[TestFixture]
public class RomanDecodeTests
{
    [TestCase(1, "I")]
    [TestCase(21, "XXI")]
    [TestCase(1990, "MCMXC")]
    [TestCase(2008, "MMVIII")]
    [TestCase(1666, "MDCLXVI")]
    public void Test(int expected, string roman)
    {
        Assert.AreEqual(expected, RomanDecode.Solution(roman));
    }
}