/*using System.Linq;

public class Kata
{
    public static string PigIt(string str)
    {
        return string.Join(" ", str.Split().Select(w => w.Length > 1 ? $"{w[1..]}{w[0]}ay" : w));
    }
}*/

using System.Text.RegularExpressions;

public class Kata
{
    public static string PigIt(string str)
    {
        return Regex.Replace(str, @"\b(\w)(\w+)", "$2$1ay");
    }
}