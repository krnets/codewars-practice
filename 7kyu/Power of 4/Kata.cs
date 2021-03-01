/*using System;

public class Power
{
    public static bool PowerOf4(object n)
    {
        return (n is long || n is int) && Convert.ToInt64(n) > 1 && Math.Log(Convert.ToInt64(n), 4) % 1 == 0;
    }
}*/

using System;
using System.Text.RegularExpressions;

public class Power
{
    public static bool PowerOf4(object n)
    {
        return (n is long || n is int) && Regex.IsMatch(Convert.ToString(Convert.ToInt64(n), 2), "^1(00)+$");
    }
}