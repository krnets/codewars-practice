using NUnit.Framework;

[TestFixture]
public static class KataTests
{
    private static void testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Examples()
    {
        testing(Kata.Palindromization("123", 2), "11");
        testing(Kata.Palindromization("123", 3), "121");
        testing(Kata.Palindromization("123", 4), "1221");
        testing(Kata.Palindromization("123", 5), "12321");
        testing(Kata.Palindromization("123", 6), "123321");
        testing(Kata.Palindromization("123", 7), "1231321");
        testing(Kata.Palindromization("123", 8), "12311321");
        testing(Kata.Palindromization("123", 9), "123121321");
        testing(Kata.Palindromization("123", 10), "1231221321");
    }

    [Test]
    public static void Error_Cases()
    {
        testing(Kata.Palindromization("", 2), "Error!");
        testing(Kata.Palindromization("123", 1), "Error!");
    }
}