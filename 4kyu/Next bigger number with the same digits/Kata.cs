using System;

public class Kata
{
    public static long NextBiggerNumber(long n)
    {
        var digits = n.ToString().ToCharArray();
        int indexFromEnd;

        for (indexFromEnd = digits.Length - 1; indexFromEnd > 0; indexFromEnd--)
        {
            var left = digits[indexFromEnd - 1];
            var right = digits[indexFromEnd];

            if (left < right)
                break;
        }

        if (indexFromEnd == 0)
            return -1L;

        int min = indexFromEnd;
        var last = digits[indexFromEnd - 1];

        for (int j = indexFromEnd + 1; j < digits.Length; j++)
            if (digits[min] > digits[j] && digits[j] > last)
                min = j;

        (digits[min], digits[indexFromEnd - 1]) = (digits[indexFromEnd - 1], digits[min]);

        Array.Sort(digits, indexFromEnd, digits.Length - indexFromEnd);

        return long.Parse(string.Concat(digits));
    }
}

/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static long NextBiggerNumber(long n)
    {
        var list = Permute(n.ToString());

        return list.Select(long.Parse)
            .OrderBy(x => x)
            .First(x => x > n);
    }

    private static List<string> Permute(string s)
    {
        var set = new HashSet<string> {s};

        for (int i = 0; i < s.Length; i++)
            set.UnionWith(Permute(s.Remove(i, 1)).Select(p => s[i] + p));

        return set.ToList();
    }
}*/