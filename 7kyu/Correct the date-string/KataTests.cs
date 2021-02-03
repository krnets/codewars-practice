using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void NullTest()
    {
        Assert.AreEqual(null, Date.Correct(null));
    }

    [Test]
    public void EmptyTest()
    {
        Assert.AreEqual("", Date.Correct(""));
    }

    [Test]
    public void InvalidFormatTests()
    {
        Assert.AreEqual(null, Date.Correct("01112016"));
        Assert.AreEqual(null, Date.Correct("01,11,2016"));
        Assert.AreEqual(null, Date.Correct("0a.1c.2016"));
    }

    [Test]
    public void CorrectionTests()
    {
        Assert.AreEqual("03.12.2016", Date.Correct("03.12.2016"));
        Assert.AreEqual("01.03.2016", Date.Correct("30.02.2016"));
        Assert.AreEqual("10.07.2015", Date.Correct("40.06.2015"));
        Assert.AreEqual("11.01.2015", Date.Correct("11.13.2014"));
        Assert.AreEqual("02.02.2015", Date.Correct("33.13.2014"));
        Assert.AreEqual("07.02.2011", Date.Correct("99.11.2010"));
        Assert.AreEqual("01.01.2017", Date.Correct("32.12.2016"));
    }
}