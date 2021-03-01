using System.Linq;

public class Kata
{
    public static int MatchArrays(int[] v, int[] r)
    {
        return v.Intersect(r).Count();
    }
}