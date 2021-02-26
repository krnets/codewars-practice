using NUnit.Framework;

class ExmapleTest
{
    [Test]
    public void FixedTest()
    {
        Assert.AreEqual(0, Kata.SquaresNeeded(0));
        Assert.AreEqual(1, Kata.SquaresNeeded(1));
        Assert.AreEqual(2, Kata.SquaresNeeded(2));
        Assert.AreEqual(2, Kata.SquaresNeeded(3));
        Assert.AreEqual(3, Kata.SquaresNeeded(4));
    }
}