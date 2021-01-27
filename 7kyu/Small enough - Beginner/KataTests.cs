using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(true, Kata.SmallEnough(new int[] {66, 101}, 200));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(false, Kata.SmallEnough(new int[] {78, 117, 110, 99, 104, 117, 107, 115}, 100));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(true, Kata.SmallEnough(new int[] {101, 45, 75, 105, 99, 107}, 107));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(true, Kata.SmallEnough(new int[] {80, 117, 115, 104, 45, 85, 112, 115}, 120));
    }
}