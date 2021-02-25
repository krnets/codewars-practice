using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string Switcheroo(string x)
    {
        // return string.Concat(x.Select(ch => ch == 'a' ? 'b' : ch == 'b' ? 'a' : ch));
        return Regex.Replace(x, "[ab]", m => m.Value == "a" ? "b" : "a");
    }
}