using NUnit.Framework;

[TestFixture]
public static class BackronymTests
{
    [Test]
    public static void TestExample1()
    {
        Assert.AreEqual("ingestable newtonian turn eager rant eager stylish turn ingestable newtonian gregarious",
            Kata.MakeBackronym("interesting"));
    }

    [Test]
    public static void TestExample2()
    {
        Assert.AreEqual("confident oscillating disturbing eager weird awesome rant stylish",
            Kata.MakeBackronym("codewars"));
    }
}