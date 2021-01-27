using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(new int[] {14, 17, 7, 3}, Kata.MenFromBoys(new int[] {7, 3, 14, 17}));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new int[] {2, 90, 95, 43, 37}, Kata.MenFromBoys(new int[] {2, 43, 95, 90, 37}));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(new int[] {20, 34, 46, 50, 43, 33}, Kata.MenFromBoys(new int[] {20, 33, 50, 34, 43, 46}));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(new int[] {72, 76, 82, 100, 91, 85}, Kata.MenFromBoys(new int[] {82, 91, 72, 76, 76, 100, 85}));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(new int[] {2, 10, 17, 15, 1}, Kata.MenFromBoys(new int[] {2, 15, 17, 15, 2, 10, 10, 17, 1, 1}));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual(new int[] {-32, -35, -39, -41}, Kata.MenFromBoys(new int[] {-32, -39, -35, -41}));
    }

    [Test]
    public void BasicTest7()
    {
        Assert.AreEqual(new int[] {-66, -64, -63, -65, -71}, Kata.MenFromBoys(new int[] {-64, -71, -63, -66, -65}));
    }

    [Test]
    public void BasicTest8()
    {
        Assert.AreEqual(new int[] {-100, -96, -94, -99}, Kata.MenFromBoys(new int[] {-94, -99, -100, -99, -96, -99}));
    }

    [Test]
    public void BasicTest9()
    {
        Assert.AreEqual(new int[] {-26, -14, -27, -49, -51, -53},
            Kata.MenFromBoys(new int[] {-53, -26, -53, -27, -49, -51, -14}));
    }

    [Test]
    public void BasicTest10()
    {
        Assert.AreEqual(new int[] {-86, -56, -30, -15, -17, -33, -45, -85},
            Kata.MenFromBoys(new int[] {-17, -45, -15, -33, -85, -56, -86, -30}));
    }

    [Test]
    public void BasicTest11()
    {
        Assert.AreEqual(new int[] {-78, -38, 12, 89}, Kata.MenFromBoys(new int[] {12, 89, -38, -78}));
    }

    [Test]
    public void BasicTest12()
    {
        Assert.AreEqual(new int[] {-90, 2, 95, 37, -43}, Kata.MenFromBoys(new int[] {2, -43, 95, -90, 37}));
    }

    [Test]
    public void BasicTest13()
    {
        Assert.AreEqual(new int[] {-12, 82, 21, 1, -61, -87}, Kata.MenFromBoys(new int[] {82, -61, -87, -12, 21, 1}));
    }

    [Test]
    public void BasicTest14()
    {
        Assert.AreEqual(new int[] {-28, 2, 76, 88, 63, -57, -85},
            Kata.MenFromBoys(new int[] {63, -57, 76, -85, 88, 2, -28}));
    }

    [Test]
    public void BasicTest15()
    {
        Assert.AreEqual(new int[] {-282, 818, 900, 928, 281, 49, -1},
            Kata.MenFromBoys(new int[] {49, 818, -282, 900, 928, 281, -282, -1}));
    }
}