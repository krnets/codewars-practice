using System;
using System.Linq;

public class Kata
{
    public static int GetLongestPalindrome(string str)
    {
        if (string.IsNullOrEmpty(str))
            return 0;

        int longest = 0;

        for (int i = 0; i < str.Length; i++)
        {
            for (int j = i + 1; j <= str.Length; j++)
                if (IsPalindrome(str[i..j]))
                    longest = Math.Max(longest, (j - i));
        }

        return longest;
    }

    private static bool IsPalindrome(string s) => s.Reverse().SequenceEqual(s);
}