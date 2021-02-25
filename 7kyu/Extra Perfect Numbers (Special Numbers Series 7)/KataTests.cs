using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(new int[] {1, 3}, Kata.ExtraPerfect(3));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new int[] {1, 3, 5}, Kata.ExtraPerfect(5));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(new int[] {1, 3, 5, 7}, Kata.ExtraPerfect(7));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(new int[] {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27}, Kata.ExtraPerfect(28));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(new int[] {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39},
            Kata.ExtraPerfect(39));
    }
}