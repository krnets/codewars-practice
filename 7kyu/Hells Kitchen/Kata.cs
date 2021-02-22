using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string Gordon(string a)
    {
        return string.Join(" ", a.Split()
            .Select(w => Regex.Replace(w.ToUpper(), "A", "@"))
            .Select(w => Regex.Replace(w, "[EIOU]", "*") + "!!!!"));
    }
}