/*using System;
using System.Text.RegularExpressions;

public class shortenMethods
{
    public static Func<object, string> ShortenNumberCreator(string[] suffixes, int baseValue)
    {
        return x =>
        {
            if (string.IsNullOrEmpty(x.ToString()))
                return string.Empty;

            if (x.GetType().IsArray)
                return string.Join(",", (x as int[])!);

            if (Regex.IsMatch(x.ToString(), @"\D$"))
                return x.ToString();

            long n = 0, i = 0;

            if (x is string)
                long.TryParse(x.ToString(), out n);

            while (n > baseValue && i < suffixes.Length - 1)
            {
                n /= baseValue;
                i++;
            }

            return n + suffixes[i];
        };
    }
}*/

using System;
using System.Text.RegularExpressions;

public class shortenMethods
{
    public static Func<object, string> ShortenNumberCreator(string[] suffixes, int baseValue)
    {
        return x =>
        {
            long n = 0, i = 0;
            var str = x.ToString();

            if (string.IsNullOrEmpty(str))
                return string.Empty;

            if (x.GetType().IsArray)
                return string.Join(",", (x as int[])!);

            if (Regex.IsMatch(str, @"\D$"))
                return str;

            if (x is string)
                long.TryParse(str, out n);

            while (n > baseValue && i < suffixes.Length - 1)
            {
                n /= baseValue;
                i++;
            }

            return n + suffixes[i];
        };
    }
}