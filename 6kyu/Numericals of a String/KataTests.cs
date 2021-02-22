using NUnit.Framework;
using System;
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("1112111121311", JomoPipi.Numericals("Hello, World!"));
    }
    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("11121111213112111131224132411122", JomoPipi.Numericals("Hello, World! It's me, JomoPipi!"));
    }
    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("11121122342", JomoPipi.Numericals("hello hello"));
    }
}