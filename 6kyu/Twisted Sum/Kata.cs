/*using System.Linq;

public class TwistedSum
{
    public static long Solution(long n)
    {
        return (long) Enumerable.Range(1, (int) n)
            .SelectMany(i => i.ToString().Select(char.GetNumericValue))
            .Sum();
    }
}*/

using System.Linq;

public class TwistedSum
{
    public static long Solution(long n)
    {
        return (long) Enumerable.Range(1, (int) n).SelectMany(i => i.ToString()).Sum(char.GetNumericValue);
    }
}

/*
using System.Linq;

public class TwistedSum
{
    public static long Solution(long n)
    {
        return string.Concat(Enumerable.Range(1, (int) n)).Sum(c => long.Parse($"{c}"));
    }
}
*/

/*public class TwistedSum
{
    public static long Solution(long n)
    {
        long sum = 0;

        for (long i = 1; i <= n; i++)
            sum += DigitSum(i);

        return sum;
    }

    private static long DigitSum(long n)
    {
        long sum = 0;

        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }

        return sum;
    }
}*/