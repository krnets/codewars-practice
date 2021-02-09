using NUnit.Framework;
[TestFixture]
public class Tests
{
    [Test]
    public void Test()
    {
        Fibonacci fib = new Fibonacci();
        Assert.AreEqual(0, fib.NthFib(1));
        Assert.AreEqual(1, fib.NthFib(2));
        Assert.AreEqual(1, fib.NthFib(3));
        Assert.AreEqual(2, fib.NthFib(4));
        Assert.AreEqual(3, fib.NthFib(5));
        Assert.AreEqual(5, fib.NthFib(6));
        Assert.AreEqual(8, fib.NthFib(7));
        Assert.AreEqual(13, fib.NthFib(8));
    }
}