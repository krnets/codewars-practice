/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int ComputeDepth(int n)
    {
        var digitsFound = new HashSet<double>();

        for (int i = 1; i <= 100; i++)
            foreach (var d in (i * n).ToString().Select(char.GetNumericValue))
            {
                digitsFound.Add(d);

                if (digitsFound.Count == 10)
                    return i;
            }

        return 0;
    }
}*/

/*
using System.Collections.Generic;

public class Kata
{
    public static int ComputeDepth(int n)
    {
        var digitsFound = new HashSet<char>();

        for (int i = 1; i <= 100; i++)
            foreach (var d in (i * n).ToString())
            {
                digitsFound.Add(d);

                if (digitsFound.Count == 10)
                    return i;
            }

        return 0;
    }
}
*/

using System.Linq;

public class Kata
{
    public static int ComputeDepth(int n)
    {
        var digits = Enumerable.Range('0', 10).ToHashSet();
        int multiples = 0;

        while (digits.Count > 0)
            foreach (char c in (++multiples * n).ToString())
                digits.Remove(c);

        return multiples;
    }
}

/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int ComputeDepth(int n)
    {
        var set = new HashSet<char>();

        return Enumerable.Range(1, 10)
            .TakeWhile(i =>
            {
                set.UnionWith((i * n).ToString());
                return set.Count < 10;
            }).Count() + 1;
    }
}*/

/*public class Kata
{
    public static int ComputeDepth(int n)
    {
        int val = 0, count = 0;

        for (int i = n; val != 1023; i += n, count++)
        {
            int current = i;

            while (current != 0)
            {
                val = val | (1 << (current % 10));
                current /= 10;
            }
        }

        return count;
    }
}*/