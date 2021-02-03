using NUnit.Framework;

[TestFixture]
public class TimeDegreesTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("30:6", TimeDegrees.ClockDegree("01:01"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("360:360", TimeDegrees.ClockDegree("00:00"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("30:18", TimeDegrees.ClockDegree("01:03"));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("30:180", TimeDegrees.ClockDegree("01:30"));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual("360:30", TimeDegrees.ClockDegree("12:05"));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual("Check your time !", TimeDegrees.ClockDegree("26:78"));
    }

    [Test]
    public void BasicTest7()
    {
        Assert.AreEqual("Check your time !", TimeDegrees.ClockDegree("23:60"));
    }

    [Test]
    public void BasicTest8()
    {
        Assert.AreEqual("Check your time !", TimeDegrees.ClockDegree("24:60"));
    }

    [Test]
    public void BasicTest9()
    {
        Assert.AreEqual("120:150", TimeDegrees.ClockDegree("16:25"));
    }

    [Test]
    public void BasicTest10()
    {
        Assert.AreEqual("150:54", TimeDegrees.ClockDegree("17:09"));
    }

    [Test]
    public void BasicTest11()
    {
        Assert.AreEqual("210:360", TimeDegrees.ClockDegree("19:00"));
    }

    [Test]
    public void BasicTest12()
    {
        Assert.AreEqual("240:204", TimeDegrees.ClockDegree("20:34"));
    }

    [Test]
    public void BasicTest13()
    {
        Assert.AreEqual("330:120", TimeDegrees.ClockDegree("23:20"));
    }

    [Test]
    public void BasicTest14()
    {
        Assert.AreEqual("Check your time !", TimeDegrees.ClockDegree("24:00"));
    }

    [Test]
    public void BasicTest15()
    {
        Assert.AreEqual("Check your time !", TimeDegrees.ClockDegree("-09:00"));
    }
}