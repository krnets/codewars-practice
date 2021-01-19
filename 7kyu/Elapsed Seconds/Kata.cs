/*using System;

public class Kata
{
    public static int ElapsedSeconds(DateTime startDate, DateTime endDate)
    {
        return (int)(endDate - startDate).TotalSeconds;
    }
}*/
using System;
public class Kata
{
    public static int ElapsedSeconds(DateTime startDate, DateTime endDate)
    {
        TimeSpan diff = endDate - startDate;
        return Convert.ToInt32(diff.TotalSeconds);
    }
}