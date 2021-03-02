/*using System;
using System.Linq;

public class Kata
{
    public static int DeepCount(object a)
    {
        return ((object[]) a).Aggregate(0, (curr, next) => curr + (next is Array ? 1 + DeepCount(next) : 1));
    }
}*/

using System.Collections;
using System.Linq;

public class Kata
{
    public static int DeepCount(object a)
    {
        return ((ICollection) a).OfType<ICollection>().Sum(DeepCount) + ((ICollection) a).Count;
    }
}