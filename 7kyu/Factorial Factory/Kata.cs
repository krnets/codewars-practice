/*using System;

public static class Kata
{
    public static int Factorial(int n)
    {
        if (n < 0) 
            throw new ArgumentException("n must be positive integer");

        int result = 1;

        while (n > 1)
        {
            result *= n;
            n--;
        }

        return result;
    }
}*/

/*using System;

public static class Kata
{
    public static int Factorial(int n)
    {
        if (n < 0)
            throw new ArgumentException("n must be positive integer");
        if (n == 0)
            return 1;

        return n * Factorial(n - 1);
    }
}*/

using System.Linq;

public static class Kata
{
    public static int Factorial(int n)
    {
        return Enumerable.Range(1, n).Aggregate(1, (a, b) => a * b);
    }
}