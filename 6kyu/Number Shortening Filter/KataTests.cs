using NUnit.Framework;

[TestFixture]
public class ShortenerTest
{
    [Test]
    public void BasicTests1000()
    {
        var filter = shortenMethods.ShortenNumberCreator(new string[] {"", "k", "m"}, 1000);

        if (filter == null)
        {
            Assert.Fail("No method to invoke!");
        }

        Assert.AreEqual("234k", filter("234324"));
        Assert.AreEqual("98m", filter("98234324"));
        Assert.AreEqual("1,2,3", filter(new int[] {1, 2, 3}));
        Assert.AreEqual("", filter(""));
        Assert.AreEqual("32424m", filter("32424234223"));
    }

    [Test]
    public void BasicTests1024()
    {
        var filter = shortenMethods.ShortenNumberCreator(new string[] {"B", "KB", "MB", "GB"}, 1024);

        if (filter == null)
        {
            Assert.Fail("No method to invoke!");
        }

        Assert.AreEqual("32B", filter("32"));
        Assert.AreEqual("2KB", filter("2100"));
        Assert.AreEqual("pippi", filter("pippi"));
        Assert.AreEqual("2100k", filter("2100k"));
        Assert.AreEqual("1023MB", filter("1073741823"));
    }
}