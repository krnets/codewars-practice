using System;

public class Solution
{
    public static int[] solve(String s)
    {
        int countUpper = 0, countLower = 0, countDigit = 0, countSpecialChars = 0;

        foreach (char c in s)
        {
            if (char.IsUpper(c)) countUpper++;
            if (char.IsLower(c)) countLower++;
            if (char.IsDigit(c)) countDigit++;
            if (!char.IsLetterOrDigit(c)) countSpecialChars++;
        }

        return new[] {countUpper, countLower, countDigit, countSpecialChars};
    }
}