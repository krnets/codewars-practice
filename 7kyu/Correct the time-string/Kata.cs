/*using System.Linq;
using System.Text.RegularExpressions;

public static class Time
{
    public static string Correct(string timeString)
    {
        if (string.IsNullOrEmpty(timeString))
            return timeString;

        if (!Regex.IsMatch(timeString, @"^\d{2}:\d{2}:\d{2}$"))
            return null;

        var parsed = timeString.Split(':').Select(int.Parse).ToArray();
        var hours = parsed[0];
        var minutes = parsed[1];
        var seconds = parsed[2];

        var totalSeconds = hours * 60 * 60;
        totalSeconds += minutes * 60;
        totalSeconds += seconds;

        return $"{totalSeconds / 60 / 60 % 24:D2}:{totalSeconds / 60 % 60:D2}:{totalSeconds % 60:D2}";
    }
}*/

using System;
using System.Linq;
using System.Text.RegularExpressions;

public static class Time
{
    public static string Correct(string timeString)
    {
        if (string.IsNullOrEmpty(timeString))
            return timeString;

        if (!Regex.IsMatch(timeString, @"^\d{2}:\d{2}:\d{2}$"))
            return null;

        var parsed = timeString.Split(':').Select(int.Parse).ToArray();
        var hours = parsed[0];
        var minutes = parsed[1];
        var seconds = parsed[2];

        return new TimeSpan(hours, minutes, seconds).ToString(@"hh\:mm\:ss");
    }
}