using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTests()
    {
        var kata = new Kata();

        Assert.AreEqual(0, kata.NumberOfCarries(543, 3456));

        Assert.AreEqual(2, kata.NumberOfCarries(1927, 6426));

        Assert.AreEqual(4, kata.NumberOfCarries(9999, 1));

        Assert.AreEqual(2, kata.NumberOfCarries(1234, 5678));
    }
}