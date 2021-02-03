public class Cogs
{
    public static double[] CogRpm(int[] cogs, int n)
    {
        int gears = cogs.Length - 1;
        var clockwiseRotation = new[] {1d, -1d};
        var firstCogRpm = cogs[n] * clockwiseRotation[n % 2] / cogs[0];
        var lastCogRpm = cogs[n] * clockwiseRotation[(gears - n) % 2] / cogs[gears];

        return new[] {firstCogRpm, lastCogRpm};
    }
}