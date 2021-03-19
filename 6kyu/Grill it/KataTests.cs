using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void GrilleIt()
    {
        Assert.AreEqual("df", Kata.Grille("abcdef", 5));
        Assert.AreEqual("", Kata.Grille("", 5));
        Assert.AreEqual("d", Kata.Grille("abcd", 1));
        Assert.AreEqual("b", Kata.Grille("0abd", 2));
        Assert.AreEqual("codewars", Kata.Grille("tcddoadepwweasresd", 77098));
    }

    [Test]
    public void Grille1()
    {
        Assert.AreEqual("e", Kata.Grille("te", 1));
        Assert.AreEqual("d", Kata.Grille("td", 1));
    }

    [Test]
    public void Grille2()
    {
        Assert.AreEqual("sf", Kata.Grille("wjsqfz", 10));
    }

    [Test]
    public void Grille3()
    {
        Assert.AreEqual("tasbmdtbjzbjtbt", Kata.Grille("cstasbmbjdztbjzbjetbtq", 1021934));
    }

    [Test]
    public void Grille4()
    {
        Assert.AreEqual("tbjzptajmtztw", Kata.Grille("pmtbwqjztptajjmaptztjstw", 3373667));
    }
}