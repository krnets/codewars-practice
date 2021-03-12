/*using System;

public class Kata
{
    public static string FormatTime(int hour)
    {
        var str = hour.ToString();

        if (str.Length < 3 || str.Length > 4)
            throw new ArgumentException();

        return str.Insert(str.Length - 2, ":");
    }
}*/

using System;

public class Kata
{
    public static string FormatTime(int hour)
    {
        if (hour < 100 || hour > 9999)
            throw new ArgumentException();

        return $"{hour:##:##}";
    }
}