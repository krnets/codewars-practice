/*using System.Collections.Generic;

public static class Kata
{
    public static string ExpandedForm(long num)
    {
        var list = new List<long>();

        for (long d, m = 1; num > 0; m *= 10)
        {
            d = (num % 10) * m;
            if (d > 0)
                list.Insert(0, d);
            num /= 10;
        }

        return string.Join(" + ", list);
    }
}*/

/*
using System.Collections.Generic;

public static class Kata
{
    public static string ExpandedForm(long num)
    {
        var stack = new Stack<long>();

        for (long digit, mult = 1; num > 0; mult *= 10)
        {
            digit = num % 10;

            if (digit > 0)
                stack.Push(digit * mult);

            num /= 10;
        }

        return string.Join(" + ", stack);
    }
}
*/

/*using System;
using System.Linq;

public static class Kata
{
    public static string ExpandedForm(long num)
    {
        var str = num.ToString();

        return string.Join(" + ", str
            .Select((x, i) => char.GetNumericValue(x) * Math.Pow(10, str.Length - i - 1))
            .Where(x => x > 0));
    }
}*/

using System.Linq;

public static class Kata
{
    public static string ExpandedForm(long num)
    {
        var numStr = num.ToString();

        return numStr.Select((c, i) => $"{c}{new string('0', numStr.Length - i - 1)}")
            .Where(s => s[0] != '0')
            .Aggregate((x, y) => $"{x} + {y}");
    }
}