using NUnit.Framework;

[TestFixture]
public class BinaryNumbersTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual("1001", BinaryNumbers.Add("111", "10"));
        Assert.AreEqual("10010", BinaryNumbers.Add("1101", "101"));
        Assert.AreEqual("100100", BinaryNumbers.Add("1101", "10111"));
        Assert.AreEqual("11", BinaryNumbers.Add("0011", "00"));
        Assert.AreEqual("11", BinaryNumbers.Add("00", "0011"));
    }
}