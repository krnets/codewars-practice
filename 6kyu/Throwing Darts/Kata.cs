using System.Linq;

public class Darts
{
    public static int ScoreThrows(double[] radii)
    {
        var bonus = radii.Length > 0 && radii.All(x => x < 5) ? 100 : 0;

        return radii.Select(x => x < 5 ? 10 : x <= 10 ? 5 : 0).Sum() + bonus;
    }
}