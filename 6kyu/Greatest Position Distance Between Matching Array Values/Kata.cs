using System.Collections.Generic;
using System.Linq;

public class GreatestDistance
{
    public static int Exec(List<int> data)
    {
        return data.Distinct().Max(x => data.LastIndexOf(x) - data.IndexOf(x));
    }
}