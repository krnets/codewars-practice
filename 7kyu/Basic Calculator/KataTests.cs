using NUnit.Framework;
using System;

[TestFixture]
public class NumbersTest
{
    [Test]
    public void Test_01()
    {
        Assert.AreEqual(11.2, Calculator.Execute(3.2, '+', 8));
    }

    [Test]
    public void Test_02()
    {
        Assert.AreEqual(-4.8, Calculator.Execute(3.2, '-', 8));
    }

    [Test]
    public void Test_03()
    {
        Assert.AreEqual(0.4, Calculator.Execute(3.2, '/', 8));
    }

    [Test]
    public void Test_04()
    {
        Assert.AreEqual(25.6, Calculator.Execute(3.2, '*', 8));
    }

    [Test]
    public void Test_10()
    {
        Assert.Throws<ArgumentException>(() => Calculator.Execute(-3, 'w', 1));
    }
}