using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(1, Kata.Divisors(1));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(3, Kata.Divisors(4));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual(2, Kata.Divisors(5));
    }

    [Test]
    public void Test10()
    {
        Assert.AreEqual(4, Kata.Divisors(10));
    }

    [Test]
    public void Test11()
    {
        Assert.AreEqual(2, Kata.Divisors(11));
    }

    [Test]
    public void Test12()
    {
        Assert.AreEqual(6, Kata.Divisors(12));
    }

    [Test]
    public void Test30()
    {
        Assert.AreEqual(8, Kata.Divisors(30));
    }

    [Test]
    public void Test54()
    {
        Assert.AreEqual(8, Kata.Divisors(54));
    }
}