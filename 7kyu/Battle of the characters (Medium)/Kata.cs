using System.Linq;

public class Kata
{
    public static string Battle(string x, string y)
    {
        var scoreX = x.Sum(Selector);
        var scoreY = y.Sum(Selector);

        return scoreX > scoreY ? x : scoreX < scoreY ? y : "Tie!";
    }

    private static double Selector(char c)
    {
        return char.IsUpper(c) ? c - 'A' + 1 : (c - 'a' + 1) / 2.0;
    }
}