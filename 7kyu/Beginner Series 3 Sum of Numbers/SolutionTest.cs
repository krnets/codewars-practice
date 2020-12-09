using NUnit.Framework;

[TestFixture]
public class SumTest1
{
    Sum s = new Sum();

    [Test]
    public void Test1()
    {
        Assert.AreEqual(1, s.GetSum(0, 1));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(-1, s.GetSum(0, -1));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(2, s.GetSum(-1, 2));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(3, s.GetSum(1, 2));
    }
}