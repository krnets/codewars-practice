using System;
using NUnit.Framework;

[TestFixture]
public class Test
{
    [Test]
    public void test1()
    {
        Assert.AreEqual(1, Kata.rowSumOddNumbers(1));
        Assert.AreEqual(74088, Kata.rowSumOddNumbers(42));
    }

    [Test]
    public void RandomInput()
    {
        Random rnd = new Random();

        for (long i = 0; i < 50; i++)
        {
            long n = rnd.Next(500) + 1;
            Assert.AreEqual(n * n * n, Kata.rowSumOddNumbers(n));
        }
    }
}