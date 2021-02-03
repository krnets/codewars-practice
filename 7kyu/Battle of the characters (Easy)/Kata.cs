using System.Linq;

public class Kata
{
    public static string Battle(string x, string y)
    {
        var scoreX = x.Sum(c => c - 'A' + 1);
        var scoreY = y.Sum(c => c - 'A' + 1);

        // return scoreX > scoreY ? x : scoreX < scoreY ? y : "Tie!";
        return scoreX == scoreY ? "Tie!" : scoreX < scoreY ? y : x;
    }
}