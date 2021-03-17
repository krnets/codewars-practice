using System;

public class Day
{
    public string countDays(DateTime d)
    {
        // var daysCount = (d - DateTime.Today.Date).Days;
        // var daysCount = (d - DateTime.Now).Days;
        var daysCount = d.Subtract(DateTime.Now).Days;

        return daysCount == 0 ? "Today is the day!" : daysCount < 0 ? "The day is in the past!" : $"{daysCount} days";
    }
}