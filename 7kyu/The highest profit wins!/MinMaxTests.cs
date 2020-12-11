using NUnit.Framework;

[TestFixture]
public class MinMaxTests
{
    [Test]
    public static void BasicTest1()
    {
        Assert.AreEqual(new[] {-1, 20}, MinMax.minMax(new[] {1, 2, 5, -1, 12, 20}));
    }

    [Test]
    public static void BasicTest2()
    {
        Assert.AreEqual(new[] {1, 5}, MinMax.minMax(new[] {1, 2, 3, 4, 5}));
    }

    [Test]
    public static void BasicTest3()
    {
        Assert.AreEqual(new[] {-3, 5}, MinMax.minMax(new[] {1, 2, -3, 4, 5}));
    }

    [Test]
    public static void BasicTest4()
    {
        Assert.AreEqual(new[] {-5, 9}, MinMax.minMax(new[] {1, 9, 3, 4, -5}));
    }

    [Test]
    public static void BasicTest5()
    {
        Assert.AreEqual(new[] {-214, 542},
            MinMax.minMax(new[] {4, 5, 29, 54, 4, 0, -214, 542, -64, 1, -3, 6, -6}));
    }

    [Test]
    public static void BasicTest6()
    {
        Assert.AreEqual(new[] {4, 4}, MinMax.minMax(new[] {4}));
    }
}