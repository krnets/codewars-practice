/*public static class ReadySet
{
    public static string Spoonerize(string str)
    {
        var words = str.Split();

        return $"{words[1][0]}{words[0][1..]} {words[0][0]}{words[1][1..]}";
    }
}*/

using System.Text.RegularExpressions;

public static class ReadySet
{
    public static string Spoonerize(string str)
    {
        return Regex.Replace(str, @"(.)(.* )(.)(.*)", "$3$2$1$4");
    }
}