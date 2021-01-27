using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(kata.maxDiff(new[] {0, 1, 2, 3, 4, 5, 6}), 6);
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(kata.maxDiff(new[] {-0, 1, 2, -3, 4, 5, -6}), 11);
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(kata.maxDiff(new[] {0, 1, 2, 3, 4, 5, 16}), 16);
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(kata.maxDiff(new[] {16}), 0);
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(kata.maxDiff(new int[] { }), 0);
    }
}