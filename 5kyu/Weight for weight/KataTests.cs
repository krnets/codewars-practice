using NUnit.Framework;

[TestFixture]
public class WeightSortTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual("2000 103 123 4444 99", WeightSort.orderWeight("103 123 4444 99 2000"));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual("11 11 2000 10003 22 123 1234000 44444444 9999",
            WeightSort.orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123"));
    }
}