/*using System;
using System.Linq;

public class Kata
{
    public static int UnluckyDays(int year)
    {
        return Enumerable.Range(1, 12)
            .Select(i => new DateTime(year, i, 13))
            .Count(dt => dt.DayOfWeek == DayOfWeek.Friday);
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static int UnluckyDays(int year)
    {
        return Enumerable.Range(1, 12)
            .Count(month => new DateTime(year, month, 13).DayOfWeek == DayOfWeek.Friday);
    }
}