/*using System.Linq;

public class Kata
{
    public static string WhatIsTheTime(string timeInMirror)
    {
        var time = timeInMirror.Split(':').Select(int.Parse).ToArray();
        var minutes = (60 - time[1]) % 60;
        var hours = (minutes > 0 ? 11 : 12) - time[0] % 12;

        return $"{(hours > 0 ? hours : 12):D2}:{minutes:D2}";
    }
}*/

using System;

public class Kata
{
    public static string WhatIsTheTime(string timeInMirror)
    {
        return DateTime.Parse("12:00").Subtract(TimeSpan.Parse(timeInMirror)).ToString("hh:mm");
    }
}