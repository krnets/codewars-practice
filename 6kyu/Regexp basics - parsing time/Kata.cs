/*using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static int? ToSeconds(this string time)
    {
        if (!Regex.IsMatch(time, @"^\d{2}(:[0-5]\d){2}$"))
            return null;

        var arr = time.Split(":").Select(int.Parse).ToArray();
        var hh = arr[0];
        var mm = arr[1];
        var ss = arr[2];

        return hh * 60 * 60 + mm * 60 + ss;
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static int? ToSeconds(this string time)
    {
        return Regex.IsMatch(time, @"^\d{2}(:[0-5]\d){2}$")
            ? time.Split(":").Select(int.Parse).Aggregate((a, b) => a * 60 + b)
            : null as int?;
    }
}