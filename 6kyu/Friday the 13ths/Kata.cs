/*using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;

public static class Kata
{
    public static string FridayTheThirteenths(int Start, int End = int.MinValue)
    {
        var dateStart = new DateTime(Start, 1, 1);
        var dateEnd = new DateTime(End == int.MinValue ? Start + 1 : End + 1, 1, 1);
        var dateCurrent = dateStart;
        var listDates = new List<DateTime>();

        while (!dateCurrent.Equals(dateEnd))
        {
            if (dateCurrent.Day == 13 && dateCurrent.DayOfWeek == DayOfWeek.Friday)
                listDates.Add(dateCurrent);

            dateCurrent = dateCurrent.AddDays(1);
        }

        return string.Join(" ", listDates.Select(date => date.ToString("d", new CultureInfo("en-US"))));
    }
}*/

using System;
using System.Globalization;
using System.Linq;

public static class Kata
{
    public static string FridayTheThirteenths(int Start, int End = int.MinValue)
    {
        var listDates = Enumerable.Range(Start, End < Start ? 1 : End - Start + 1)
            .SelectMany(year => Enumerable.Range(1, 12)
                .Select(month => new DateTime(year, month, 13))
                .Where(dateTime => dateTime.DayOfWeek == DayOfWeek.Friday));

        var ci = new CultureInfo("en-US");

        return string.Join(" ", listDates.Select(date => date.ToString("d", ci)));
    }
}