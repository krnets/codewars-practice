using NUnit.Framework;

[TestFixture]
public class FactorialTests
{
    [Test]
    public void FactorialOf0ShouldBe1()
    {
        Assert.AreEqual(1, Kata.Factorial(0));
    }

    [Test]
    public void FactorialOf1ShouldBe1()
    {
        Assert.AreEqual(1, Kata.Factorial(1));
    }

    [Test]
    public void FactorialOf2ShouldBe2()
    {
        Assert.AreEqual(2, Kata.Factorial(2));
    }

    [Test]
    public void FactorialOf3ShouldBe6()
    {
        Assert.AreEqual(6, Kata.Factorial(3));
    }
}