using NUnit.Framework;

[TestFixture]
public static class MaxRotateTests
{
    private static void Testing(long actual, long expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Testing(MaxRotate.MaxRot(38458215), 85821534);
    }

    [Test]
    public static void Test2()
    {
        Testing(MaxRotate.MaxRot(195881031), 988103115);
    }

    [Test]
    public static void Test3()
    {
        Testing(MaxRotate.MaxRot(896219342), 962193428);
    }

    [Test]
    public static void Test4()
    {
        Testing(MaxRotate.MaxRot(69418307), 94183076);
    }
}