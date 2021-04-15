/*using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;

public class HumanTimeFormat
{
    public static string formatDuration(int seconds)
    {
        if (seconds == 0) return "now";

        int secInMin = 60;
        int secInHour = 60 * secInMin;
        int secInDay = 24 * secInHour;
        int secInYear = 365 * secInDay;

        int ss = seconds % secInMin;
        int mm = (seconds % secInHour) / secInMin;
        int hh = (seconds % secInDay) / secInHour;
        int dd = (seconds % secInYear) / secInDay;
        int yy = seconds / secInYear;

        int[] nums = {ss, mm, hh, dd, yy};
        string[] words = {"second", "minute", "hour", "day", "year"};
        var stack = new Stack<string>();
        var sb = new StringBuilder();

        for (int i = 0; i < nums.Length; i++)
            if (nums[i] > 0)
                stack.Push($"{nums[i]} {words[i]}{(nums[i] > 1 ? "s" : "")}");

        if (stack.Count == 1)
            return sb.Append(stack.Pop()).ToString();

        while (stack.Count > 1)
            sb.Append(stack.Pop()).Append(", ");

        sb.Append("and ").Append(stack.Pop());

        return Regex.Replace(sb.ToString(), ", and", " and");
    }
}*/

using System;
using System.Collections.Generic;
using System.Linq;

public class HumanTimeFormat
{
    public static string formatDuration(int seconds)
    {
        if (seconds == 0) return "now";

        var time = TimeSpan.FromSeconds(seconds);
        var map = new Dictionary<string, int>
        {
            ["year"] = time.Days / 365, ["day"] = time.Days % 365, ["hour"] = time.Hours, ["minute"] = time.Minutes, ["second"] = time.Seconds
        };
        var list = new List<string>();

        foreach ((string key, int value) in map)
            if (value > 0)
                list.Add($"{value} {key}{(value > 1 ? "s" : "")}");

        var sl = string.Join(", ", list.SkipLast(2));
        var tl = string.Join(" and ", list.TakeLast(2));

        return list.Count == 1 ? list.First() : $"{(sl.Length > 0 ? $"{sl}, " : "")}{tl}";
    }
}