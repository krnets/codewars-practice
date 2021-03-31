using NUnit.Framework;

[TestFixture]
public class CombinePathsUriTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("/", Kata.CombinePathsUri());
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("/google/search/test", Kata.CombinePathsUri("google", "search", "test"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("/testing/empty/parts/and/with/different/slashes",
            Kata.CombinePathsUri("   /testing", "", "", "  \\  empty", "\\parts/", " and ", "",
                "with/different\\slashes    "));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("/../complex/path/with/slashes/inside/./complex/path/with/back/slashes/inside",
            Kata.CombinePathsUri(" .. ", "/complex/path/with/slashes/inside/", " . ",
                "\\complex\\path\\with\\back\\slashes\\inside\\"));
    }
}