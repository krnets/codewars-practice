using System;
using System.Linq;

class Kata
{
    public static int MaxNumber(int n)
    {
        //return Convert.ToInt32(string.Concat(n.ToString().OrderByDescending(char.GetNumericValue)));
        return Convert.ToInt32(string.Concat(n.ToString().OrderByDescending(c => c)));
    }
}