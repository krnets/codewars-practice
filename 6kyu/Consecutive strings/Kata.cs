using System;
using System.Collections.Generic;
using System.Linq;

public class LongestConsecutives
{
    public static String LongestConsec(string[] strarr, int k)
    {
        var list = new List<string>();
        int longest = 0;

        for (int i = 0; i <= strarr.Length - k; i++)
        {
            var joinedStr = string.Concat(strarr.Skip(i).Take(k));
            // var joinedStr = string.Join("", strarr, i, k);
            list.Add(joinedStr);
            longest = Math.Max(longest, joinedStr.Length);
        }

        return list.FirstOrDefault(s => s.Length == longest) ?? string.Empty;
    }
}