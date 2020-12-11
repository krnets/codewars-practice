using NUnit.Framework;

[TestFixture]
public static class NbDigTests
{
    private static void testing(int actual, int expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void test1()
    {
        testing(CountDig.NbDig(5750, 0), 4700);
    }

    [Test]
    public static void test2()
    {
        testing(CountDig.NbDig(11011, 2), 9481);
    }

    [Test]
    public static void test3()
    {
        testing(CountDig.NbDig(12224, 8), 7733);
    }

    [Test]
    public static void test4()
    {
        testing(CountDig.NbDig(11549, 1), 11905);
    }

    [Test]
    public static void test5()
    {
        testing(CountDig.NbDig(14550, 7), 8014);
    }

    [Test]
    public static void test6()
    {
        testing(CountDig.NbDig(8304, 7), 3927);
    }

    [Test]
    public static void test7()
    {
        testing(CountDig.NbDig(10576, 9), 7860);
    }

    [Test]
    public static void test8()
    {
        testing(CountDig.NbDig(12526, 1), 13558);
    }

    [Test]
    public static void test9()
    {
        testing(CountDig.NbDig(7856, 4), 7132);
    }

    [Test]
    public static void test10()
    {
        testing(CountDig.NbDig(14956, 1), 17267);
    }
}
