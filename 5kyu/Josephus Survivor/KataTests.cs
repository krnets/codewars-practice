using NUnit.Framework;

[TestFixture]
public static class JosephusSurvivorTests
{
    private static void Testing(int actual, int expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Testing(JosephusSurvivor.JosSurvivor(7, 3), 4);
    }

    [Test]
    public static void Test2()
    {
        Testing(JosephusSurvivor.JosSurvivor(11, 19), 10);
    }

    [Test]
    public static void Test3()
    {
        Testing(JosephusSurvivor.JosSurvivor(40, 3), 28);
    }

    [Test]
    public static void Test4()
    {
        Testing(JosephusSurvivor.JosSurvivor(14, 2), 13);
    }

    [Test]
    public static void Test5()
    {
        Testing(JosephusSurvivor.JosSurvivor(100, 1), 100);
    }

    [Test]
    public static void Test6()
    {
        Testing(JosephusSurvivor.JosSurvivor(1, 300), 1);
    }

    [Test]
    public static void Test7()
    {
        Testing(JosephusSurvivor.JosSurvivor(2, 300), 1);
    }

    [Test]
    public static void Test8()
    {
        Testing(JosephusSurvivor.JosSurvivor(5, 300), 1);
    }

    [Test]
    public static void Test9()
    {
        Testing(JosephusSurvivor.JosSurvivor(7, 300), 7);
    }

    [Test]
    public static void Test10()
    {
        Testing(JosephusSurvivor.JosSurvivor(300, 300), 265);
    }
}