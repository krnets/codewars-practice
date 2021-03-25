using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void Tx1()
    {
        Assert.AreEqual("", Main.toexuto(""));
    }

    [Test]
    public void Tx2()
    {
        Assert.AreEqual("liitotolie", Main.toexuto("little"));
    }

    [Test]
    public void Tx3()
    {
        Assert.AreEqual("BaIGe", Main.toexuto("BIG"));
    }

    [Test]
    public void Tx4()
    {
        Assert.AreEqual("Toheiso iso a toesoto. Toheiso iso oniliyu a toesoto.",
            Main.toexuto("This is a test. This is only a test."));
    }

    [Test]
    public void Tx5()
    {
        Assert.AreEqual("Toheiso iso a toesoto tooo.", Main.toexuto("This is a test too."));
    }

    [Test]
    public void Tx6()
    {
        Assert.AreEqual("Caani yuou roeada toheiso afetoero ito'so toroanisoliatoeda?",
            Main.toexuto("Can you read this after it's translated?"));
    }

    [Test]
    public void Tx7()
    {
        Assert.AreEqual(
            "Yuou miayu liaugehe ato Baoba anida Miaroyu feoro heavuinige sotoroanigee soounidainige niamieso ini Eniigeeliiisoohee, bauto yuouro niamie poroobaabaliyu soounidaso feuniniyu tooo!",
            Main.toexuto(
                "You may laugh at Bob and Mary for having strange sounding names in Enigeliisohe, but your name probably sounds funny too!"));
    }
}