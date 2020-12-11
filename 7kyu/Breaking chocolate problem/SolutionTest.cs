using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SimpleTest1()
    {
        Assert.AreEqual(24, Kata.BreakChocolate(5, 5));
    }

    [Test]
    public void SimpleTest2()
    {
        Assert.AreEqual(0, Kata.BreakChocolate(1, 1));
    }

    [Test]
    public void SimpleTest3()
    {
        Assert.AreEqual(0, Kata.BreakChocolate(1, 1));
    }

    [Test]
    public void SimpleTest4()
    {
        Assert.AreEqual(0, Kata.BreakChocolate(0, 0), "What If I Told You There is No Chocolate?");
    }

    [Test]
    public void SimpleTest5()
    {
        Assert.AreEqual(5, Kata.BreakChocolate(6, 1));
    }
}