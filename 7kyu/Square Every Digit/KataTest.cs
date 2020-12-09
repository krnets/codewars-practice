using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void KataSquareDigitsTest1()
    {
        Assert.AreEqual(811181, Kata.SquareDigits(9119));
    }

    [Test]
    public void KataSquareDigitsTest2()
    {
        Assert.AreEqual(9414, Kata.SquareDigits(3212));
    }

    [Test]
    public void KataSquareDigitsTest3()
    {
        Assert.AreEqual(4114, Kata.SquareDigits(2112));
    }
}