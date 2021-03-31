using NUnit.Framework;
using System;

[TestFixture]
public class Tests
{
    private Kata kata;

    [Test]
    public void SystemClock_IsEqualWithDateTimeNow()
    {
        Assert.AreEqual(DateTime.Now.Year, new SystemClock().Now.Year);
        Assert.AreEqual(DateTime.Now.Month, new SystemClock().Now.Month);
        Assert.AreEqual(DateTime.Now.Day, new SystemClock().Now.Day);
    }

    [Test]
    public void GetAgeFromDOB()
    {
        kata = new Kata(new StaticClock(new DateTime(2008, 09, 3)));
        Assert.AreEqual(24, kata.GetAgeFromDOB(new DateTime(1984, 04, 23)));
    }
}