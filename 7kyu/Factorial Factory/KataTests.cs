using NUnit.Framework;
using System;

[TestFixture]
public class FactorialTests
{
    [Test]
    public void Test1()
    {
        // Don't forget the special cases!
        Assert.AreEqual(Kata.Factorial(0), 1, "What is '0!' ?");
        Assert.AreEqual(Kata.Factorial(1), 1, "Your math may be incorrect");
        Assert.AreEqual(Kata.Factorial(2), 2, "Your math may be incorrect");
        Assert.AreEqual(Kata.Factorial(5), 120, "Your math may be incorrect");
        Assert.Throws(Is.InstanceOf<Exception>(), () => Kata.Factorial(-1),
            "Exception not thrown for negative number!");
    }
}