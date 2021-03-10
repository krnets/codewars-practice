using NUnit.Framework;

[TestFixture]
public class ModSystemTests
{
    [Test]
    public void Test1()
    {
        int[] lst = new int[] {8, 7, 5, 3};
        Assert.AreEqual("-3--5--2--1-", ModSystem.fromNb2Str(187, lst));
    }

    [Test]
    public void Test2()
    {
        int[] lst = new int[] {2, 3, 5};
        Assert.AreEqual("-1--2--1-", ModSystem.fromNb2Str(11, lst));
    }

    [Test]
    public void Test3()
    {
        int[] lst = new int[] {2, 3, 4};
        Assert.AreEqual("Not applicable", ModSystem.fromNb2Str(6, lst));
    }

    [Test]
    public void Test4()
    {
        int[] lst = new int[] {2, 3};
        Assert.AreEqual("Not applicable", ModSystem.fromNb2Str(7, lst));
    }
}