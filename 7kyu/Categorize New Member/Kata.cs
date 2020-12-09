using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static IEnumerable<string> OpenOrSenior(int[][] data)
    {
        return data.Select(member => member[0] >= 55 && member[1] > 7 ? "Senior" : "Open");
    }
}