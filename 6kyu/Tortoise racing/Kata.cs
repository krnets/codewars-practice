/*public class Tortoise
{
    public static int[] Race(int v1, int v2, int g)
    {
        if (v1 >= v2) return null;

        int secondsInHour = 60 * 60;
        g = secondsInHour * g / (v2 - v1);
        int hour = g / secondsInHour;
        int min = g % secondsInHour / 60;
        int sec = g % 60;

        return new[] {hour, min, sec};
    }
}*/

public class Tortoise
{
    public static int[] Race(int v1, int v2, int g)
    {
        if (v1 >= v2)
            return null;

        int secondsInHour = 60 * 60;
        var ts = System.TimeSpan.FromSeconds(g * secondsInHour / (v2 - v1));

        return new[] {ts.Hours, ts.Minutes, ts.Seconds};
    }
}