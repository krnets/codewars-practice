/*
using System;
using System.Linq;

public class KataCalculator
{
    public static int SolvedKatasSince(DateTime registrationDate, DateTime currentDate)
    {
        return Enumerable
            .Range(0, (currentDate - registrationDate).Days)
            .Select(x => registrationDate.AddDays(x).DayOfWeek)
            .Count(dow => dow != DayOfWeek.Saturday && dow != DayOfWeek.Sunday);
    }
}
*/

using System;

public class KataCalculator
{
    public static int SolvedKatasSince(DateTime registrationDate, DateTime currentDate)
    {
        int count = 0;

        for (var i = registrationDate; i < currentDate; i = i.AddDays(1))
            if (i.DayOfWeek != DayOfWeek.Saturday && i.DayOfWeek != DayOfWeek.Sunday)
                count++;

        return count;
    }
}