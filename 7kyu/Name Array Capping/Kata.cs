using System.Globalization;
using System.Linq;

public static class Kata
{
    public static string[] CapMe(string[] strings)
    {
        var ti = CultureInfo.CurrentCulture.TextInfo;

        return strings.Select(name => ti.ToTitleCase(name.ToLower())).ToArray();
    }
}