/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static long[] NumbersWithDigitInside(long x, long d)
    {
        var list = new List<long>();
        var digit = d.ToString();

        for (var i = 1; i <= x; i++)
            if (i.ToString().Contains(digit))
                list.Add(i);

        long count = list.Count;
        long sum = list.Sum();
        long product = list.DefaultIfEmpty(0).Aggregate((a, b) => a * b);

        return new[] {count, sum, product};
    }
}*/

public class Kata
{
    public static long[] NumbersWithDigitInside(long x, long d)
    {
        long count = 0, sum = 0, product = 1;
        var digit = d.ToString();

        for (var i = 1; i <= x; i++)
            if (i.ToString().Contains(digit))
            {
                count++;
                sum += i;
                product *= i;
            }

        return new[] {count, sum, count > 0 ? product : 0};
    }
}