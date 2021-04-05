using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(string.Join(", ", new long[] {1, 2, 3}), string.Join(", ", Kata.SplitOddAndEven(123)));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(string.Join(", ", new long[] {22, 3}), string.Join(", ", Kata.SplitOddAndEven(223)));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(string.Join(", ", new long[] {111}), string.Join(", ", Kata.SplitOddAndEven(111)));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(string.Join(", ", new long[] {13579}), string.Join(", ", Kata.SplitOddAndEven(13579)));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(string.Join(", ", new long[] {135, 246}), string.Join(", ", Kata.SplitOddAndEven(135246)));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual(string.Join(", ", new long[] {1, 2, 3, 4, 5, 6}),
            string.Join(", ", Kata.SplitOddAndEven(123456)));
    }
}