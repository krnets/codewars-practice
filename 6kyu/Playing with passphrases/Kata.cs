using System;
using System.Linq;
using static System.Char;

public class PlayPass
    {
    public static string playPass(string s, int n)
    {
        return string.Concat(s.Select(c =>
                IsLetter(c) ? (char) ((c - 'A' + n) % 26 + 'A') :
                IsDigit(c) ? (char) (Math.Abs(c - '0' - 9) + '0') : c)
            .Select((c, i) => i % 2 == 0 ? c : ToLower(c))
            .Reverse());
    }
}

/*
using System;
using System.Linq;
using System.Text;

public class PlayPass
{
    public static string playPass(string s, int n)
    {
        var sb = new StringBuilder();

        for (int i = 0; i < s.Length; i++)
        {
            char c = s[i];

            if (char.IsDigit(c))
                sb.Append(Math.Abs(char.GetNumericValue(c) - 9));

            else if (char.IsLetter(c))
            {
                var shifted = (char) (((c - 'A' + n) % 26 + 'A'));

                sb.Append(i % 2 == 0 ? shifted : char.ToLower(shifted));
            }
            else sb.Append(c);
        }

        return string.Concat(sb.ToString().Reverse());
    }
}
*/

/*using System;

public class PlayPass
{
    public static string playPass(string s, int n)
    {
        var passPhrase = new char[s.Length];

        for (int i = 0; i < s.Length; i++)
        {
            char c = s[i];

            if (char.IsDigit(c))
            {
                passPhrase[i] = (char) (Math.Abs(c - '0' - 9) + '0');
                // passPhrase[i] = (char) (Math.Abs(9 - char.GetNumericValue(c)) + '0');
            }
            else if (char.IsLetter(c))
            {
                var shifted = (char) (((c - 'A' + n) % 26 + 'A'));

                passPhrase[i] = (i % 2 == 0 ? shifted : char.ToLower(shifted));
            }
            else passPhrase[i] = c;
        }

        Array.Reverse(passPhrase);

        return new string(passPhrase);
    }
}*/