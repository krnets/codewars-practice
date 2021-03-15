/*class Kata
{
    public static bool HasSubpattern(string str)
    {
        return (str + str)[1..^1].Contains(str);
    }
}*/

using System.Text.RegularExpressions;

class Kata
{
    public static bool HasSubpattern(string str)
    {
        return Regex.IsMatch(str, @"^(.*)\1+$");
    }
}