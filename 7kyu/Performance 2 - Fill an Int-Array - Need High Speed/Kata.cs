using System.Linq;

public static class Kata
{
    private const int Limit = 4_000_000;

    public static int[] Performance()
    {
        return Enumerable.Range(0, Limit).ToArray();
    }
}