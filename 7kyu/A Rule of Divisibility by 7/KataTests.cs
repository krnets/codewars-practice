using NUnit.Framework;

[TestFixture]
public class DivSevenTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(new long[] {10, 2}, DivSeven.Seven(1021));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(new long[] {7, 2}, DivSeven.Seven(1603));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(new long[] {35, 1}, DivSeven.Seven(371));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(new long[] {42, 1}, DivSeven.Seven(483));
    }
}