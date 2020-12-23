using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public static void Example1()
    {
        Assert.AreEqual("ThIs", Kata.ToWeirdCase("This"));
    }

    [Test]
    public static void Example2()
    {
        Assert.AreEqual("Is", Kata.ToWeirdCase("is"));
    }

    [Test]
    public static void Example3()
    {
        Assert.AreEqual("ThIs Is A TeSt", Kata.ToWeirdCase("This is a test"));
    }
}