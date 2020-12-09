using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public static void ExampleTest1()
    {
        Assert.AreEqual(false, Kata.IsSquare(-1), "negative numbers aren't square numbers");
    }

    [Test]
    public static void ExampleTest2()
    {
        Assert.AreEqual(false, Kata.IsSquare(3), "3 isn't a square number");
    }

    [Test]
    public static void ExampleTest3()
    {
        Assert.AreEqual(true, Kata.IsSquare(4), "4 is a square number");
    }

    [Test]
    public static void ExampleTest4()
    {
        Assert.AreEqual(true, Kata.IsSquare(25), "25 is a square number");
    }

    [Test]
    public static void ExampleTest5()
    {
        Assert.AreEqual(false, Kata.IsSquare(26), "26 isn't a square number");
    }
}