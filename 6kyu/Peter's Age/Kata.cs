/*
using System;

public class Kata
{
    public static string HowOld(DateTime birthday)
    {
        var today = DateTime.Today;
        var difference = today
            .AddDays(-birthday.Day)
            .AddMonths(-birthday.Month)
            .AddYears(-birthday.Year);

        var years = difference.Year;
        var months = difference.Month;
        var days = difference.Day;

        return $"Peter is {years} years, {months} months and {days} days old";
    }
}
*/


/*
using System;

public class Kata
{
    public static string HowOld(DateTime birthday)
    {
        var current = DateTime.Now;
        var years = current.Year - birthday.Year;
        var months = current.Month - birthday.Month;
        var days = current.Day - birthday.Day;

        if (months < 0)
        {
            months += 12;
            years--;
        }

        if (days < 0)
        {
            days += DateTime.DaysInMonth(birthday.Year, birthday.Month);
            months--;
        }

        return $"Peter is {years} years, {months} months and {days} days old";
    }
}
*/

using System;

public class Kata
{
    public static string HowOld(DateTime birthday)
    {
        var current = DateTime.Now;
        var years = current.Year - birthday.Year;
        var months = current.Month - birthday.Month;
        var days = current.Day - birthday.Day;

        if (months < 0)
        {
            months += 12;
            years--;
        }

        return $"Peter is {years} years, {months} months and {days} days old";
    }
}