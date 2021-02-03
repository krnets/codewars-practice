/*
using System.Linq;
using System.Text.RegularExpressions;

public class TimeDegrees
{
    public static string ClockDegree(string s)
    {
        var array = Regex.Split(s, "\\:").Select(int.Parse).ToArray();
        int hours = array[0];
        int minutes = array[1];

        if (hours < 0 || hours >= 24 || minutes < 0 || minutes >= 60)
            return "Check your time !";

        int hh = 360 / 12 * hours;
        int mm = 360 / 60 * minutes;

        return $"{(hh % 360 == 0 ? 360 : hh % 360)}:{(mm % 360 == 0 ? 360 : mm % 360)}";
    }
}
*/

/*using System.Linq;

public class TimeDegrees
{
    public static string ClockDegree(string s)
    {
        var array = s.Split(':').Select(int.Parse).ToArray();
        int hours = array[0];
        int minutes = array[1];

        if (hours < 0 || hours >= 24 || minutes < 0 || minutes >= 60)
            return "Check your time !";

        int hh = 360 / 12 * hours;
        int mm = 360 / 60 * minutes;

        return $"{(hh % 360 == 0 ? 360 : hh % 360)}:{(mm % 360 == 0 ? 360 : mm % 360)}";
    }
}*/

using System;

public class TimeDegrees
{
    public static string ClockDegree(string s)
    {
        if (!DateTime.TryParse(s, out var time))
            return "Check your time !";

        int hourDegree = (360 / 12 * time.Hour) % 360;
        int minuteDegree = (360 / 60 * time.Minute);

        return $"{(hourDegree > 0 ? hourDegree : 360)}:{(minuteDegree > 0 ? minuteDegree : 360)}";
    }
}