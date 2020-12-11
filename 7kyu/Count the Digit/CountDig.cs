/*
using System.Linq;
using System.Text.RegularExpressions;

public class CountDig
{
    public static int NbDig(int n, int d)
    {
        var digits = string.Concat(Enumerable.Range(0, n + 1).Select(i => i * i));

        return Regex.Matches(digits, d.ToString()).Count;
    }
}
*/

using System.Linq;

public class CountDig
{
    public static int NbDig(int n, int d)
    {
        char digit = char.Parse(d.ToString());

        return Enumerable.Range(0, n + 1).Select(i => (i * i).ToString().Count(c => c == digit)).Sum();
    }
}

/*using System.Linq;

public class CountDig
{
    public static int NbDig(int n, int d)
    {
        return Enumerable.Range(0, n + 1).Select(i => (i * i).ToString().Count(c => char.GetNumericValue(c) == d)).Sum();
    }
}*/