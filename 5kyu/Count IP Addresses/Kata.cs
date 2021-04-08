using System;
using System.Linq;

public class CountIPAddresses
{
    public static long IpsBetween(string start, string end)
    {
        return start.Split(".")
            // .Zip(end.Split("."), (s, e) => Convert.ToInt32(e) - Convert.ToInt32(s))
            .Zip(end.Split("."), (s, e) => int.Parse(e) - int.Parse(s))
            .Reverse()
            .Select((x, i) => x * (i > 0 ? (long) Math.Pow(256, i) : 1))
            .Sum();
    }
}