using NUnit.Framework;
using System;

[TestFixture]
public class UnitTest
{ 
   
    [Test]
    public void TestRowOne()
    {
        Assert.AreEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", Kata.GetRow(1));      
    }
    [Test]
    public void TestRowTwentySix()
    {
        Assert.AreEqual("ZZZZZZZZZZZZZZZZZZZZZZZZZZ", Kata.GetRow(26));      
    }
    [Test]
    public void TestRowFifthteen()
    {
        Assert.AreEqual("OOOOOOOOOOOOOOOPQRSTUVWXYZ", Kata.GetRow(15));      
    }
    [Test]
    public void TestRowTwentySeven()
    {
        Assert.AreEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", Kata.GetRow(27));      
    }
}