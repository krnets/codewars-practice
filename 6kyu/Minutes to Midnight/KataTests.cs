using NUnit.Framework;
using System;

[TestFixture]
public class MinuteTest
{
    [Test]
    public void exampleTests()
    {
        Minute m = new Minute();
        DateTime testDate = DateTime.Now.Date.AddHours(12);
        Assert.AreEqual("720 minutes", m.countMinutes(testDate));

        testDate = DateTime.Now.Date.AddHours(23).AddMinutes(59);
        Assert.AreEqual("1 minute", m.countMinutes(testDate));
    }
}