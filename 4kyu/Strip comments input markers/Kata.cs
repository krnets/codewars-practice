/*using System.Linq;

public class StripCommentsSolution
{
    public static string StripComments(string text, string[] commentSymbols)
    {
        return string.Join("\n", text.Split("\n")
            .Select(s => string.Concat(s.TakeWhile(c => !commentSymbols.Contains(c.ToString()))).TrimEnd()));
    }
}*/

/*using System;
using System.Linq;

public class StripCommentsSolution
{
    public static string StripComments(string text, string[] commentSymbols)
    {
        return string.Join("\n", text.Split("\n")
            .Select(s => s.Split(commentSymbols, StringSplitOptions.None).First().TrimEnd()));
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class StripCommentsSolution
{
    public static string StripComments(string text, string[] commentSymbols)
    {
        var pattern = $"[{string.Concat(commentSymbols)}].*";

        return string.Join("\n", text.Split("\n")
            .Select(s => Regex.Replace(s, pattern, "").TrimEnd()));
    }
}