using System;
using NUnit.Framework;

[TestFixture]
public class CheckChooseTests
{
    [Test]
    public void Test1()
    {
        Console.WriteLine("****** Basic Tests");
        Assert.AreEqual(2, CheckChoose.Checkchoose(6, 4));
        Assert.AreEqual(1, CheckChoose.Checkchoose(4, 4));
        Assert.AreEqual(3, CheckChoose.Checkchoose(35, 7));
        Assert.AreEqual(-1, CheckChoose.Checkchoose(4, 2));
        Assert.AreEqual(-1, CheckChoose.Checkchoose(36, 7));
    }
}