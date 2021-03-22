using NUnit.Framework;

[TestFixture]
public class SystemTests
{ 
    [Test]
    public void Test1()
    {
        Assert.AreEqual(1, SystemOfEq.Solution(9,3));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(1, SystemOfEq.Solution(14,28));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(0, SystemOfEq.Solution(4, 20));
    }
}