using System;
using System.Linq;
using System.Text.RegularExpressions;

public static class Date
{
    public static string Correct(string dateString)
    {
        if (string.IsNullOrEmpty(dateString))
            return dateString;

        if (!Regex.IsMatch(dateString, @"\d\d\.\d\d\.\d{4}"))
            return null;

        var array = Regex.Split(dateString, @"\.").Select(int.Parse).ToArray();
        var day = array[0];
        var month = array[1];
        var year = array[2];

        return new DateTime().AddYears(year - 1).AddMonths(month - 1).AddDays(day - 1).ToString("dd.MM.yyyy");
    }
}