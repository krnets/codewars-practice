using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTests()
    {
        var kata = new Kata();

        Assert.AreEqual(52, kata.DeleteDigit(152));
        Assert.AreEqual(5, kata.DeleteDigit(52));
        Assert.AreEqual(101, kata.DeleteDigit(1001));
        Assert.AreEqual(1, kata.DeleteDigit(10));
    }
}