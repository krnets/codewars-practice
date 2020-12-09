/*public class Sum
{
    public int GetSum(int a, int b)
    {
        int sum = 0;

        if (a > b)
            (a, b) = (b, a);

        for (int i = a; i <= b; i++)
            sum += i;

        return sum;
    }
}*/

/*using System;
using System.Linq;

public class Sum
{
    public int GetSum(int a, int b)
    {
        return Enumerable.Range(Math.Min(a, b), Math.Max(a, b) - Math.Min(a, b) + 1).Sum();
    }
}*/

using System;

public class Sum
{
    public int GetSum(int a, int b)
    {
        return (a + b) * (Math.Abs(a - b) + 1) / 2;
    }
}