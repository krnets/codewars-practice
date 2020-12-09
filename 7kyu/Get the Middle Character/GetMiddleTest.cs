using NUnit.Framework;

[TestFixture]
public class GetMiddleTest
{
    [Test]
    public void GenericTest0()
    {
        Assert.AreEqual("", Kata.GetMiddle(""));
    }
    [Test]
    public void GenericTest1()
    {
        Assert.AreEqual("es", Kata.GetMiddle("test"));
    }

    [Test]
    public void GenericTest2()
    {
        Assert.AreEqual("t", Kata.GetMiddle("testing"));
    }

    [Test]
    public void GenericTest3()
    {
        Assert.AreEqual("dd", Kata.GetMiddle("middle"));
    }

    [Test]
    public void GenericTest4()
    {
        Assert.AreEqual("A", Kata.GetMiddle("A"));
    }
}