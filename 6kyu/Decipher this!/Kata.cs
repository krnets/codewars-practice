using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string DecipherThis(string s)
    {
        return string.Join(" ", s.Split(" ")
            .Select(word => Regex.Replace(word, "\\d+", m => $"{(char) int.Parse(m.Value)}"))
            .Select(word => Regex.Replace(word, "^(.)(.)(.*)(.)$", "$1$4$3$2")));
    }
}

/*using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string DecipherThis(string s)
    {
        return string.Join(" ", s.Split(" ")
            .Select(word => Regex.Replace(word, "^(\\d+)(.?)(.*?)(.?)$", m =>
                (char) int.Parse(m.Groups[1].Value) +
                m.Groups[4].Value + m.Groups[3].Value + m.Groups[2].Value)));
    }
}*/