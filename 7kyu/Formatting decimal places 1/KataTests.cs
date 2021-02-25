using NUnit.Framework;
using System;
  
[TestFixture]
public class NumbersTest
{
    [Test]
    public void Test_01()
    {
        Assert.AreEqual(10.12, Numbers.TwoDecimalPlaces(10.1289767789));
    }

    [Test]
    public void Test_Negative_02()
    {
        Assert.AreEqual(-7488.83, Numbers.TwoDecimalPlaces(-7488.83485834983));
    }
}