using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(10, Kata.Fibonacci(10));
    }
}