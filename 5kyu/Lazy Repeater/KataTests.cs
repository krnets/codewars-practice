using NUnit.Framework;
using System;

[TestFixture]
public class Sample_Tests
{
    [Test]
    public void SampleTest()
    {
        Func<char> abc = Kata.MakeLooper("abc");
        // Two iterations of looper
        // 1
        Assert.AreEqual('a', abc());
        Assert.AreEqual('b', abc());
        Assert.AreEqual('c', abc());
        // 2
        Assert.AreEqual('a', abc());
        Assert.AreEqual('b', abc());
        Assert.AreEqual('c', abc());
    }
}