using System.Linq;

public static class Kata
{
    public static int GolfScoreCalculator(string par, string score)
    {
        // return score.Select(c => (int) c).Sum() - par.Select(c => (int) c).Sum();
        // return score.Select((c, i) => c - par[i]).Sum();
        return score.Zip(par, (a, b) => a - b).Sum();
    }
}