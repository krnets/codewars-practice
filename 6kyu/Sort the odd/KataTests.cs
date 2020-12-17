using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(new int[] {1, 3, 2, 8, 5, 4}, Kata.SortArray(new int[] {5, 3, 2, 8, 1, 4}));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new int[] {1, 3, 5, 8, 0}, Kata.SortArray(new int[] {5, 3, 1, 8, 0}));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(new int[] { }, Kata.SortArray(new int[] { }));
    }
}