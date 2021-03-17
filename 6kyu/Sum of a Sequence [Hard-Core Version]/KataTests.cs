using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(12, Kata.SequenceSum(2, 6, 2));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(15, Kata.SequenceSum(1, 5, 1));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(5, Kata.SequenceSum(1, 5, 3));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(-5, Kata.SequenceSum(-1, -5, -3));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(0, Kata.SequenceSum(16, 15, 3));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual(-26, Kata.SequenceSum(-24, -2, 22));
    }

    [Test]
    public void BasicTest7()
    {
        Assert.AreEqual(-2, Kata.SequenceSum(-2, 4, 658));
    }

    [Test]
    public void BasicTest8()
    {
        Assert.AreEqual(469436517521190, Kata.SequenceSum(780, 68515438, 5));
    }
}