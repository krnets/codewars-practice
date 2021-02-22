/*using System;

public class Suite2
{
    public static string game(long n)
    {
        return $"[{(n % 2 == 0 ? $"{n / 2 * n}" : $"{Math.Pow(n, 2)}, 2")}]";
    }
}*/


/*
public class Suite2
{
    public static string game(long n)
    {
        return $"[{(n % 2 == 0 ? $"{n / 2 * n}" : $"{n * n}, 2")}]";
    }
}
*/

public class Suite2
{
    public static string game(long n)
    {
        return "[" + (n % 2 == 0 ? $"{n / 2 * n}" : $"{n * n}, 2") + "]";
    }
}