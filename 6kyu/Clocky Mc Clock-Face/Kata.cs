/*public class Dinglemouse
{
    public static string WhatTimeIsIt(double angle)
    {
        var hourAngle = 360 / 12.0;
        var minuteAngle = hourAngle / 60;
        var hh = (int) (angle / hourAngle);
        var mm = (int) (angle / minuteAngle) % 60;

        return $"{(hh > 0 ? hh : 12):D2}:{mm:D2}";
    }
}*/


using System;

public class Dinglemouse
{
    public static string WhatTimeIsIt(double angle)
    {
        return DateTime.Today.Add(TimeSpan.FromHours(angle / 360 * 12)).ToString("hh:mm");
    }
}