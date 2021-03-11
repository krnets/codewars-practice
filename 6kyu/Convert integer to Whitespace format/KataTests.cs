using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(unbleach(" \t\n"), unbleach(Kata.WhitespaceNumber(1)));
        Assert.AreEqual(unbleach(" \n"), unbleach(Kata.WhitespaceNumber(0)));
        Assert.AreEqual(unbleach("\t\t\n"), unbleach(Kata.WhitespaceNumber(-1)));
        Assert.AreEqual(unbleach(" \t \n"), unbleach(Kata.WhitespaceNumber(2)));
        Assert.AreEqual(unbleach("\t\t\t\n"), unbleach(Kata.WhitespaceNumber(-3)));
    }

    private string unbleach(string ws)
    {
        return ws.Replace(" ", "[space]").Replace("\t", "[tab]").Replace("\n", "[LF]");
    }
}