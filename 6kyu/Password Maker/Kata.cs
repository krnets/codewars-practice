/*using System;
using System.Collections.Generic;
using System.Linq;

public class Dinglemouse
{
    public static string MakePassword(int len, bool flagUpper, bool flagLower, bool flagDigit)
    {
        var rnd = new Random();
        var set = new HashSet<char>();

        var upper = Enumerable.Range('A', 26).OrderBy(_ => rnd.Next()).Select(i => (char) i).ToList();
        var lower = Enumerable.Range('a', 26).OrderBy(_ => rnd.Next()).Select(i => (char) i).ToList();
        var digits = Enumerable.Range('0', 10).OrderBy(_ => rnd.Next()).Select(i => (char) i).ToList();
        int digitCount = 10;

        while (set.Count < len)
        {
            if (flagUpper)
            {
                set.Add(upper[0]);
                upper.RemoveAt(0);
            }

            if (flagLower)
            {
                set.Add(lower[0]);
                lower.RemoveAt(0);
            }

            if (flagDigit && digitCount > 0)
            {
                set.Add(digits[0]);
                digits.RemoveAt(0);
                digitCount--;
            }
        }

        return string.Concat(set.Take(len));
    }
}*/

using System;
using System.Collections.Generic;
using System.Linq;

public class Dinglemouse
{
    public static string MakePassword(int len, bool flagUpper, bool flagLower, bool flagDigit)
    {
        var rnd = new Random();
        var password = new List<char>();

        var upper = Enumerable.Range('A', 26).OrderBy(_ => rnd.Next()).Select(i => (char) i).ToList();
        var lower = Enumerable.Range('a', 26).OrderBy(_ => rnd.Next()).Select(i => (char) i).ToList();
        var digits = Enumerable.Range('0', 10).OrderBy(_ => rnd.Next()).Select(i => (char) i).ToList();
        int digitCount = 10;

        while (password.Count < len)
        {
            if (flagUpper)
            {
                password.Add(upper[0]);
                upper.RemoveAt(0);
            }

            if (flagLower)
            {
                password.Add(lower[0]);
                lower.RemoveAt(0);
            }

            if (flagDigit && digitCount > 0)
            {
                password.Add(digits[0]);
                digits.RemoveAt(0);
                digitCount--;
            }
        }

        return string.Concat(password.Take(len));
    }
}