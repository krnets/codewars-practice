using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTests()
    {
        var kata = new Kata();

        Assert.AreEqual(4, kata.HammingDistance(25, 87));

        Assert.AreEqual(4, kata.HammingDistance(-25, -87));

        Assert.AreEqual(4, kata.HammingDistance(256, 302));

        Assert.AreEqual(4, kata.HammingDistance(543, 634));

        Assert.AreEqual(7, kata.HammingDistance(34013, 702));
    }
}