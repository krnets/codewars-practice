using System.Collections.Generic;

public class Kata
{
    public static string Collatz(int n)
    {
        var list = new List<int> {n};

        while (n > 1)
        {
            if (n % 2 == 0)
                n /= 2;
            else
                n = (3 * n) + 1;
            list.Add(n);
        }

        return string.Join("->", list);
    }
}