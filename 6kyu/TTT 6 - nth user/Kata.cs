using System;
using System.Linq;

public class Kata
{
    public static string UserNumber(int n)
    {
        return string.Concat(Convert.ToString(n, 8).Select(c => (char) (c < '4' ? c : c + 1)));
    }
}