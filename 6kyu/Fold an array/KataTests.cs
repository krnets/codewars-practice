using NUnit.Framework;

public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        var input = new int[] {1, 2, 3, 4, 5};
        var expected = new int[] {6, 6, 3};
        Assert.AreEqual(string.Join(",", expected), string.Join(",", Kata.FoldArray(input, 1)));
    }

    [Test]
    public void BasicTest2()
    {
        var input = new int[] {1, 2, 3, 4, 5};
        var expected = new int[] {9, 6};
        Assert.AreEqual(string.Join(",", expected), string.Join(",", Kata.FoldArray(input, 2)));
    }

    [Test]
    public void BasicTest3()
    {
        var input = new int[] {1, 2, 3, 4, 5};
        var expected = new int[] {15};
        Assert.AreEqual(string.Join(",", expected), string.Join(",", Kata.FoldArray(input, 3)));
    }

    [Test]
    public void BasicTest4()
    {
        var input = new int[] {-9, 9, -8, 8, 66, 23};
        var expected = new int[] {14, 75, 0};
        Assert.AreEqual(string.Join(",", expected), string.Join(",", Kata.FoldArray(input, 1)));
    }
}