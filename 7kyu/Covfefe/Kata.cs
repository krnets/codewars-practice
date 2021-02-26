using System.Text.RegularExpressions;

public static class Solution
{
    public static string Covfefe(string tweet)
    {
        // return tweet.Contains("coverage") ? Regex.Replace(tweet, "coverage", "covfefe") : tweet + " covfefe";
        return tweet.Contains("coverage") ? tweet.Replace("coverage", "covfefe") : tweet + " covfefe";
    }
}