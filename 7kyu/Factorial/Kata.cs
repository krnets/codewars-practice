/*using System;

public static class Kata
{
    public static int Factorial(int n)
    {
        if (n < 0 || n > 12) throw new ArgumentOutOfRangeException();

        return n <= 1 ? 1 : n * Factorial(n - 1);
    }
}*/

using System;
using System.Linq;

public static class Kata
{
    public static int Factorial(int n)
    {
        if (n < 0 || n > 12) throw new ArgumentOutOfRangeException();

        return Enumerable.Range(1, n).Aggregate(1, (x, y) => x * y);
    }
}