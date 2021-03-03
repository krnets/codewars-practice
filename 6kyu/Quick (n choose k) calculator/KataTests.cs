using NUnit.Framework;
using System;
using System.Numerics;

public class QuickCalcTest
{
    [Test]
    public void BasicTests1()
    {
        Console.WriteLine("****** Basic tests small numbers");
        Assert.AreEqual(new BigInteger(1), QuickCalc.Choose(1, 1));
        Assert.AreEqual(new BigInteger(5), QuickCalc.Choose(5, 4));
        Assert.AreEqual(new BigInteger(252), QuickCalc.Choose(10, 5));
        Assert.AreEqual(new BigInteger(0), QuickCalc.Choose(10, 20));
        Assert.AreEqual(new BigInteger(2598960), QuickCalc.Choose(52, 5));
    }

    [Test]
    public void BasicTests2()
    {
        Console.WriteLine("****** Basic tests larger numbers");
        Assert.AreEqual(new BigInteger(17310309456440L), QuickCalc.Choose(100, 10));
        Assert.AreEqual(new BigInteger(2573031125L), QuickCalc.Choose(500, 4));
        Assert.AreEqual(new BigInteger(166167000), QuickCalc.Choose(1000, 3));
        Assert.AreEqual(new BigInteger(55098996177225L), QuickCalc.Choose(200, 8));
        Assert.AreEqual(new BigInteger(962822846700L), QuickCalc.Choose(300, 6));
    }
}