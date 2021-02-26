using System;
using NUnit.Framework;

[TestFixture]
public class PowerTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(true, Power.PowerOf4(4));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(true, Power.PowerOf4(16));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(false, Power.PowerOf4(1));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(false, Power.PowerOf4(3.1415));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(false, Power.PowerOf4("4"));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual(false, Power.PowerOf4(null));
    }


    [Test]
    public void BasicTrueTests()
    {
        Assert.AreEqual(true, Power.PowerOf4(4));
        Assert.AreEqual(true, Power.PowerOf4(16));
        Assert.AreEqual(true, Power.PowerOf4(64));
        Assert.AreEqual(true, Power.PowerOf4(1024));
    }

    [Test]
    public void BasicFalseTests()
    {
        Assert.AreEqual(false, Power.PowerOf4(1));
        Assert.AreEqual(false, Power.PowerOf4(5));
        Assert.AreEqual(false, Power.PowerOf4(0));
        Assert.AreEqual(false, Power.PowerOf4(-4));
        Assert.AreEqual(false, Power.PowerOf4(-1));
        Assert.AreEqual(false, Power.PowerOf4(81));
        Assert.AreEqual(false, Power.PowerOf4(25));
        Assert.AreEqual(false, Power.PowerOf4(17));

        Assert.AreEqual(false, Power.PowerOf4(double.NaN));
        Assert.AreEqual(false, Power.PowerOf4(false));
        Assert.AreEqual(false, Power.PowerOf4(new object()));
        Assert.AreEqual(false, Power.PowerOf4(null));
        Assert.AreEqual(false, Power.PowerOf4(5.4));
        Assert.AreEqual(false, Power.PowerOf4(-24.234));
        Assert.AreEqual(false, Power.PowerOf4(DateTime.Now));
    }

    [Test]
    public void RandomTests()
    {
        Random rand = new Random();
        for (var i = 0; i < 30; i++)
        {
            var number = rand.Next(1, 20);

            Assert.AreEqual(MyPowerOf4(number), Power.PowerOf4(number));
            Assert.AreEqual(MyPowerOf4(number * 4), Power.PowerOf4(number * 4));
            Assert.AreEqual(MyPowerOf4(Convert.ToInt64(Math.Pow(4, number))),
                Power.PowerOf4(Convert.ToInt64(Math.Pow(4, number))));
        }
    }

    private bool MyPowerOf4(object n)
    {
        if (n == null)
            return false;

        switch (Type.GetTypeCode(n.GetType()))
        {
            case TypeCode.Byte:
            case TypeCode.SByte:
            case TypeCode.UInt64:
            case TypeCode.Int16:
            case TypeCode.Int32:
            case TypeCode.Int64:
                break;
            default:
                return false;
        }

        var number = (double) Convert.ToInt64(n);

        if (number < 0)
            return false;

        while (number > 4)
            number /= 4;

        return number == 4;
    }
}