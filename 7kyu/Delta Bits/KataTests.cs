using NUnit.Framework;

[TestFixture]
public class DeltaBitsTest
{
    [Test]
    public void TestFixedValues()
    {
        Assert.AreEqual(2, DeltaBits.ConvertBits(31, 14), "ConvertBits(31, 14)");
        Assert.AreEqual(3, DeltaBits.ConvertBits(7, 17), "ConvertBits(7, 17)");
        Assert.AreEqual(5, DeltaBits.ConvertBits(31, 0), "ConvertBits(31, 0)");
        Assert.AreEqual(0, DeltaBits.ConvertBits(0, 0), "ConvertBits(0, 0)");
        Assert.AreEqual(0, DeltaBits.ConvertBits(127681, 127681), "ConvertBits(127681, 127681)");
        Assert.AreEqual(13, DeltaBits.ConvertBits(312312312, 5645657), "ConvertBits(312312312, 5645657)");
        Assert.AreEqual(17, DeltaBits.ConvertBits(43, 2009989843), "ConvertBits(43, 2009989843)");
    }
}