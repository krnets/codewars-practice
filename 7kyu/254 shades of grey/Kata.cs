using System;
using System.Linq;

public static class Kata
{
    public static string[] ShadesOfGrey(int n)
    {
        // return Enumerable.Range(1, Math.Min(254, Math.Max(0, n)))
        return Enumerable.Range(1, Math.Clamp(n, 0, 254))
            .Select(i => $"#{i:x2}{i:x2}{i:x2}")
            .ToArray();
    }
}

/*using System.Linq;

public static class Kata
{
    public static string[] ShadesOfGrey(int n)
    {
        return Enumerable.Range(1, 254).Take(n)
            .Select(i => $"#{i:x2}{i:x2}{i:x2}")
            .ToArray();
    }
}*/