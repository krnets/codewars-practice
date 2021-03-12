/*using static System.Math;
using static System.Text.RegularExpressions.Regex;

public class Kata
{
    public static int DeadAntCount(string ants)
    {
        return ants == null || string.IsNullOrEmpty(ants = ants.Replace("ant", ""))
            ? 0
            : Max(Max(Replace(ants, "[^a]", "").Length,
                    Replace(ants, "[^n]", "").Length),
                Replace(ants, "[^t]", "").Length);
    }
}*/

/*using System.Linq;

public class Kata
{
    public static int DeadAntCount(string ants)
    {
        return ants == null ? 0 : "ant".Select(c => ants.Replace("ant", "").Count(h => c == h)).Max();
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static int DeadAntCount(string ants)
    {
        return ants == null || string.IsNullOrEmpty(ants = ants.Replace("ant", ""))
            ? 0
            : "ant".Max(c => Regex.Replace(ants, $"[^{c}]", "").Length);
    }
}