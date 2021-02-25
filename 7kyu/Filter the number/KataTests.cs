using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public static void FixedTest()
    {
        Assert.AreEqual(123, Kata.FilterString("123"), "Just return the numbers");
        Assert.AreEqual(123, Kata.FilterString("a1b2c3"), "Just return the numbers");
        Assert.AreEqual(123, Kata.FilterString("aa1bb2cc3dd"), "Just return the numbers");
    }
}