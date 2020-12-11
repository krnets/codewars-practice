public class Evaporator
{
    public static int evaporator(double content, double evap_per_day, double threshold)
    {
        double percentageLoss = (100 - evap_per_day) / 100;
        threshold = content * (threshold / 100);
        int days = 0;

        while (content > threshold)
        {
            content *= percentageLoss;
            days++;
        }

        return days;
    }
}

/*using System;

public class Evaporator
{
    public static int evaporator(double content, double evap_per_day, double threshold)
    {
        return (int) Math.Ceiling(Math.Log(threshold / 100) / Math.Log(1 - evap_per_day / 100));
    }
}*/