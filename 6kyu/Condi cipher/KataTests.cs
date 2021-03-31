using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleEncodeTest1()
    {
        Assert.AreEqual("jx", Kata.Encode("on", "cryptogam", 10));
    }

    [Test]
    public void SampleEncodeTest2()
    {
        Assert.AreEqual("cytgmdfmbk", Kata.Encode("cryptogram", "cryptogam", 0));
    }

    [Test]
    public void SampleEncodeTest3()
    {
        Assert.AreEqual("jx wnz xrkvz jnd l ufd vwcz.", Kata.Encode("on the first day i got lost.", "cryptogam", 10));
    }

    [Test]
    public void SampleEncodeTest4()
    {
        Assert.AreEqual("n ggka cvssb bfe esz omgdyr bqqva",
            Kata.Encode("i will never eat any grapes again", "superkey", 4));
    }

    [Test]
    public void SampleDecodeTest1()
    {
        Assert.AreEqual("on", Kata.Decode("jx", "cryptogam", 10));
    }

    [Test]
    public void SampleDecodeTest2()
    {
        Assert.AreEqual("....", Kata.Decode("....", "cryptogam", 10));
    }

    [Test]
    public void SampleDecodeTest3()
    {
        Assert.AreEqual("sit", Kata.Decode("abc", "keykeykeykey", 10));
    }

    [Test]
    public void SampleDecodeTest4()
    {
        Assert.AreEqual(",sit", Kata.Decode(",abc", "keykeykeykey", 10));
    }

    [Test]
    public void SampleDecodeTest5()
    {
        Assert.AreEqual("on the first day i got lost.", Kata.Decode("jx wnz xrkvz jnd l ufd vwcz.", "cryptogam", 10));
    }

    [Test]
    public void SampleDecodeTest6()
    {
        Assert.AreEqual("i will never eat any grapes again",
            Kata.Decode("n ggka cvssb bfe esz omgdyr bqqva", "superkey", 30));
    }

    [Test]
    public void SampleDecodeTest7()
    {
        Assert.AreEqual("zva nguhbmmgydx.s,ok se,rmafz vpedgbua",
            Kata.Decode("qvf cmnxmdkjfca.p,ab mf,byokf vjhwpcyb", "nqhbfgmi", 28));
    }
}