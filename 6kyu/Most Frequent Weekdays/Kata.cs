using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string[] MostFrequentDays(int year)
    {
        var dayOfWeekCounter = new Dictionary<DayOfWeek, int>()
        {
            {DayOfWeek.Monday, 0},
            {DayOfWeek.Tuesday, 0},
            {DayOfWeek.Wednesday, 0},
            {DayOfWeek.Thursday, 0},
            {DayOfWeek.Friday, 0},
            {DayOfWeek.Saturday, 0},
            {DayOfWeek.Sunday, 0},
        };
        var dateCurrent = new DateTime(year, 1, 1);
        var dateNextYear = new DateTime(year + 1, 1, 1);

        while (dateCurrent < dateNextYear)
        {
            dayOfWeekCounter[dateCurrent.DayOfWeek]++;
            dateCurrent = dateCurrent.AddDays(1);
        }

        int max = dayOfWeekCounter.Values.Max();

        return dayOfWeekCounter.Where(p => p.Value == max).Select(x => x.Key.ToString()).ToArray();
    }
}