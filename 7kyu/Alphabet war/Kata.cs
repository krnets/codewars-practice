public class Kata
{
    public static string AlphabetWar(string fight)
    {
        int leftScore = 0, rightScore = 0;
        string leftLetterPower = "sbpw", righLetterPower = "zdqm";

        foreach (char c in fight)
        {
            leftScore += leftLetterPower.IndexOf(c) + 1;
            rightScore += righLetterPower.IndexOf(c) + 1;
        }

        return leftScore != rightScore
            ? $"{(leftScore > rightScore ? "Left" : "Right")} side wins!"
            : "Let's fight again!";
        /*
        return leftScore == rightScore
            ? "Let's fight again!"
            : $"{(leftScore > rightScore ? "Left" : "Right")} side wins!";
    */
    }
}