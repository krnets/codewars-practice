using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(1, Kata.F(0));
        Assert.AreEqual(0, Kata.M(0));

        Assert.AreEqual(1, Kata.F(1));
        Assert.AreEqual(0, Kata.M(1));

        Assert.AreEqual(2, Kata.F(2));
        Assert.AreEqual(1, Kata.M(2));
    }
}