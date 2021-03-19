using NUnit.Framework;

[TestFixture]
public class DiamondTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(
            "      1      \n     121     \n    12321    \n   1234321   \n  123454321  \n 12345654321 \n1234567654321\n 12345654321 \n  123454321  \n   1234321   \n    12321    \n     121     \n      1      ",
              //   "123456_123456__12345___12345__1234_____1234__123_______123__12_________12__1__
            Diamond.Pattern(7));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("1", Diamond.Pattern(1));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("  1  \n 121 \n12321\n 121 \n  1  ", Diamond.Pattern(3));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("", Diamond.Pattern(0));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual("", Diamond.Pattern(-25));
    }
}