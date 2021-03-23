using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest()
    {
        string[] deck = DeckOfCards.BuildDeck();
        Assert.AreEqual(52, deck.Length, "Your deck should have 52 cards");
    }
}