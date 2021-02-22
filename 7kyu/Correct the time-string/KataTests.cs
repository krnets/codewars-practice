using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void NullTest()
    {
        Assert.AreEqual(null, Time.Correct(null));
    }

    [Test]
    public void EmptyTest()
    {
        Assert.AreEqual("", Time.Correct(""));
    }

    [Test]
    public void InvalidFormatTests()
    {
        Assert.AreEqual(null, Time.Correct("001122"));
        Assert.AreEqual(null, Time.Correct("00;11;22"));
        Assert.AreEqual(null, Time.Correct("0a:1c:22"));
    }

    [Test]
    public void CorrectionTest1()
    {
        Assert.AreEqual("09:10:01", Time.Correct("09:10:01"));
    }

    [Test]
    public void CorrectionTest2()
    {
        Assert.AreEqual("12:10:10", Time.Correct("11:70:10"));
    }

    [Test]
    public void CorrectionTest3()
    {
        Assert.AreEqual("20:40:39", Time.Correct("19:99:99"));
    }

    [Test]
    public void CorrectionTest4()
    {
        Assert.AreEqual("00:01:01", Time.Correct("24:01:01"));
    }

    [Test]
    public void CorrectionTest5()
    {
        Assert.AreEqual("04:01:01", Time.Correct("52:01:01"));
    }
}