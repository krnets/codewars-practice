/*using System;

public static class StringExtensions
{
    public const string Base36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static int Parse(this string value, int fromBase)
    {
        if (value == null)
            throw new ArgumentNullException();

        if (string.IsNullOrEmpty(value) || fromBase < 2 || fromBase > 36)
            throw new ArgumentException();

        value = value.ToUpper().Trim();
        int pos = 0;
        int ans = 0;

        while (pos < value.Length && char.IsLetterOrDigit(value[pos]))
        {
            var digit = value.Substring(pos, 1);
            int i = Base36.IndexOf(digit);

            if (i >= 0 && i < fromBase)
            {
                if (ans < 0 && ans * fromBase < int.MaxValue)
                    throw new OverflowException();

                ans *= fromBase;
                ans += i;
                pos++;
            }
            else throw new FormatException();
        }

        return ans;
    }
}*/

using System;
using System.Linq;

public static class StringExtensions
{
    public static int Parse(this string value, int fromBase)
    {
        if (value == null)
            throw new ArgumentNullException();

        if (value.Trim() == string.Empty || fromBase < 2 || fromBase > 36)
            throw new ArgumentException();

        return (int) value.Aggregate(0u, (acc, c) => Convert.ToUInt32(acc * fromBase + GetNumValueFrom(c, fromBase)));
    }

    private static double GetNumValueFrom(char c, int fromBase)
    {
        var num = (c <= '9') ? char.GetNumericValue(c) : char.ToUpper(c) + 10 - 'A';

        return (num < 0 || num >= fromBase) ? throw new FormatException() : num;
    }
}