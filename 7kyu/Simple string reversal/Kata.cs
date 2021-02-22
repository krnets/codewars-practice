using System;
using System.Linq;
using System.Text;

public class Solution
{
    public static String solve(String s)
    {
        using var reversed = s.Where(char.IsLetter).Reverse().GetEnumerator();
        var sb = new StringBuilder();

        foreach (char c in s)
        {
            if (c == ' ')
                sb.Append(' ');
            else
            {
                reversed.MoveNext();
                sb.Append(reversed.Current);
            }
        }

        return sb.ToString();
    }
}