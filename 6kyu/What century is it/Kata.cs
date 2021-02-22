/*public class Kata
{
    public static string WhatCentury(string year)
    {
        var y = int.Parse(year);
        var century = y / 100 + (y % 100 == 0 ? 0 : 1);

        return century > 3 && century < 21 ? century + "th" :
            century % 10 == 1 ? century + "st" :
            century % 10 == 2 ? century + "nd" :
            century % 10 == 3 ? century + "rd" : century + "th";
    }
}*/

using System.Collections.Generic;

public class Kata
{
    public static string WhatCentury(string year)
    {
        var y = int.Parse(year);
        var century = y / 100 + (y % 100 == 0 ? 0 : 1);
        var suffix = new Dictionary<int, string> {[1] = "st", [2] = "nd", [3] = "rd"};

        return century > 3 && century < 21 ? century + "th" : century + suffix.GetValueOrDefault(century % 10, "th");
    }
}