using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(true, Kata.One(new int[] {1, 2, 3, 4, 5}, v => v < 2));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(false, Kata.One(new int[] {1, 2, 3, 4, 5}, v => v % 2 != 0));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(false, Kata.One(new int[] {1, 2, 3, 4, 5}, v => v > 5));
    }
}