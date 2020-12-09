using NUnit.Framework;

[TestFixture]
public static class TwoToOneTests
{
    [Test]
    public static void test1()
    {
        Assert.AreEqual("aehrsty", TwoToOne.Longest("aretheyhere", "yestheyarehere"));
    }

    [Test]
    public static void test2()
    {
        Assert.AreEqual("abcdefghilnoprstu", TwoToOne.Longest("loopingisfunbutdangerous", "lessdangerousthancoding"));
    }

    [Test]
    public static void test3()
    {
        Assert.AreEqual("acefghilmnoprstuy", TwoToOne.Longest("inmanylanguages", "theresapairoffunctions"));
    }
}