using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static string Liftoff(List<int> instructions)
    {
        return string.Join(" ", instructions.OrderByDescending(x => x).ToArray()) + " liftoff!";
    }
}