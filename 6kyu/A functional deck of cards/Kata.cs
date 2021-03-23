using System.Linq;

public class DeckOfCards
{
    private static string[] suits = {"hearts", "spades", "clubs", "diamonds"};
    private static string[] ranks = {"ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"}; 
    public static string[] BuildDeck() => ranks.SelectMany(r => suits.Select(s => $"{r} of {s}")).ToArray();
}