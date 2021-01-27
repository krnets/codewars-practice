/*
using System.Collections.Generic;
using System.Linq;

public static class ArrayMethods
{
    public static TSource Head<TSource>(this List<TSource> list)
    {
        //return list.ElementAt(0);
        return list[0];
    }

    public static List<TSource> Tail<TSource>(this List<TSource> list)
    {
        // return list.Count > 0 ? list.Skip(1).ToList() : list;
        return list.GetRange(1, list.Count - 1);
    }

    public static List<TSource> Init<TSource>(this List<TSource> list)
    {
        //return list.Count > 0 ? list.Take(list.Count - 1).ToList() : list;
        return list.GetRange(0, list.Count - 1);
    }

    public static TSource Last_<TSource>(this List<TSource> list)
    {
        // return list.Count > 0 ? list.Last() : list.First();
        return list[^1];
    }
}
*/

using System.Collections.Generic;

public static class ArrayMethods
{
    public static TSource Head<TSource>(this List<TSource> list) => list[0];

    public static List<TSource> Tail<TSource>(this List<TSource> list) => list.GetRange(1, list.Count - 1);

    public static List<TSource> Init<TSource>(this List<TSource> list) => list.GetRange(0, list.Count - 1);

    public static TSource Last_<TSource>(this List<TSource> list) => list[^1];
}
