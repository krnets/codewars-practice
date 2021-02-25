using System;

public static class Kata
{
    public static bool AmIAfraid(string day, int num)
    {
        return day switch
        {
            "Monday"    => num == 12,
            "Tuesday"   => num > 95,
            "Wednesday" => num == 34,
            "Thursday"  => num == 0,
            "Friday"    => num % 2 == 0,
            "Saturday"  => num == 56,
            "Sunday"    => Math.Abs(num) == 666,
            _           => false
        };
    }
}