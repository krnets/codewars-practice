using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static int Solve(List<int> list)
    {
        return list.Distinct().Sum();
    }
}