/*public class MaxRotate
{
    public static long MaxRot(long n)
    {
        var numStr = n.ToString();

        for (int i = 0; i < numStr.Length - 1; i++)
        {
            numStr = numStr[0..i] + numStr[(i + 1)..] + numStr[i];
            var current = long.Parse(numStr);

            if (current > n)
                n = current;
        }

        return n;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class MaxRotate
{
    public static long MaxRot(long n)
    {
        var list = new List<long> {n};
        var numStr = n.ToString();

        for (int i = 0; i < numStr.Length - 1; i++)
        {
            numStr = numStr[0..i] + numStr[(i + 1)..] + numStr[i];
            list.Add(long.Parse(numStr));
        }

        return list.Max();
    }
}