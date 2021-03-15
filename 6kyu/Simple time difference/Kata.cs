/*using System.Linq;

public class Solution
{
    public static string solve(string[] arr)
    {
        var alarms = arr.Select(GetMinutesTotal).OrderBy(x => x).ToList();
        int minutesInDay = 24 * 60;
        alarms.Add(alarms[0] + minutesInDay);

        var maxDiff = Enumerable.Range(1, alarms.Count - 1).Max(i => alarms[i] - alarms[i - 1]) - 1;
        var hh = maxDiff / 60;
        var mm = maxDiff % 60;

        return $"{hh:D2}:{mm:D2}";
    }

    private static int GetMinutesTotal(string s)
    {
        var time = s.Split(":").Select(int.Parse).ToArray();
        int hours = time[0], minutes = time[1];

        return hours * 60 + minutes;
    }
}*/

using System;
using System.Linq;

public class Solution
{
    public static string solve(string[] arr)
    {
        var alarms = arr.Select(DateTime.Parse).OrderBy(time => time).ToArray();

        return alarms.Prepend(alarms.Last().AddDays(-1))
            .Zip(alarms, (a, b) => b - a.AddMinutes(1))
            .Max()
            .ToString(@"hh\:mm");
    }
}