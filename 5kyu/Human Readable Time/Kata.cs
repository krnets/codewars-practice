/*public static class TimeFormat
{
    public static string GetReadableTime(int seconds)
    {
        int HH = seconds / 60 / 60;
        int MM = (seconds / 60) % 60;
        int SS = seconds % 60;

        return $"{HH:d2}:{MM:d2}:{SS:d2}";
    }
}*/

using System;

public static class TimeFormat
{
    public static string GetReadableTime(int seconds)
    {
        var t = TimeSpan.FromSeconds(seconds);

        return $"{(int) t.TotalHours:d2}:{t.Minutes:d2}:{t.Seconds:d2}";
    }
}