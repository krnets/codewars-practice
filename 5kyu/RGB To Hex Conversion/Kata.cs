/*using System;

public class Kata
{
    public static string Rgb(int r, int g, int b)
    {
        r = Math.Max(0, Math.Min(255, r));
        g = Math.Max(0, Math.Min(255, g));
        b = Math.Max(0, Math.Min(255, b));

        return $"{r:X2}{g:X2}{b:X2}";
    }
}*/

/*using System;

public class Kata
{
    public static string Rgb(int r, int g, int b)
    {
        r = Math.Clamp(r, 0, 255);
        g = Math.Clamp(g, 0, 255);
        b = Math.Clamp(b, 0, 255);

        return $"{r:X2}{g:X2}{b:X2}";
    }
}*/

using System.Linq;

public class Kata
{
    public static string Rgb(int r, int g, int b)
    {
        r = Clamp(r, 0, 255);
        g = Clamp(g, 0, 255);
        b = Clamp(b, 0, 255);
        var hex = string.Concat(Enumerable.Range(0, 10).Select(i => $"{i}")).Concat("ABCDEF").ToArray();

        return $"{hex[r / 16]}{hex[r % 16]}{hex[g / 16]}{hex[g % 16]}{hex[b / 16]}{hex[b % 16]}";
    }

    private static int Clamp(int val, int min, int max)
    {
        return val < min ? 0 : val > max ? 255 : val;
    }
}