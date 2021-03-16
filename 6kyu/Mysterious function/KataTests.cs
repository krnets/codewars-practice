using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(2, Kata.GetNum(300));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(4, Kata.GetNum(90783));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(0, Kata.GetNum(123321));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(8, Kata.GetNum(89282350306));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual(5, Kata.GetNum(3479283469));
    }
}