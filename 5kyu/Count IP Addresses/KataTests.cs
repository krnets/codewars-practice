using NUnit.Framework;

public class CountIPAddressesTest
{
    [Test]
    public void SmapleTest1()
    {
        Assert.AreEqual(50, CountIPAddresses.IpsBetween("10.0.0.0", "10.0.0.50"));
    }

    [Test]
    public void SmapleTest2()
    {
        Assert.AreEqual(246, CountIPAddresses.IpsBetween("20.0.0.10", "20.0.1.0"));
    }

    [Test]
    public void SmapleTest3()
    {
        Assert.AreEqual(12282896, CountIPAddresses.IpsBetween("180.224.178.190", "181.156.30.206"));
    }
}