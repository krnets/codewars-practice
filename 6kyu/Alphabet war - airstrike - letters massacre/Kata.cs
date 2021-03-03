using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string AlphabetWar(string fight)
    {
        var leftWins = "Left side wins!";
        var rightWins = "Right side wins!";
        var tie = "Let's fight again!";
        var letterPower = new Dictionary<char, int>()
        {
            ['w'] = -4, ['p'] = -3, ['b'] = -2, ['s'] = -1,
            ['m'] = 4,  ['q'] = 3,  ['d'] = 2,  ['z'] = 1,
        };
        int score = Regex.Replace(fight, @"(.?\*+.?)", "")
            .Sum(c => letterPower.GetValueOrDefault(c, 0));

        return score < 0 ? leftWins : score > 0 ? rightWins : tie;
    }
}