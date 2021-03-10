using NUnit.Framework;

[TestFixture]
public class PizzaTest
{
    [Test]
    public void testNegative()
    {
        Assert.AreEqual(-1, Pizza.maxPizza(-2));
    }

    [Test]
    public void testZero()
    {
        Assert.AreEqual(1, Pizza.maxPizza(0));
    }

    [Test]
    public void test3()
    {
        Assert.AreEqual(7, Pizza.maxPizza(3));
    }
}