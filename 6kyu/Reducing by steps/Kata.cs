using System;
using System.Collections.Generic;
using System.Linq;

public class Operarray
{
    public static long gcdi(long x, long y) => y == 0 ? Math.Abs(x) : gcdi(y, x % y);
    public static long lcmu(long a, long b) => (Math.Abs(a * b) / gcdi(a, b));
    public static long som(long a, long b) => a + b;
    public static long maxi(long a, long b) => a > b ? a : b;
    public static long mini(long a, long b) => a < b ? a : b;
    public static long oper(Func<long, long, long> fct, long a, long b) => fct(a, b);

    /*
    public static long[] OperArray(Func<long, long, long> fct, long[] arr, long init)
    {
        var result = new long[arr.Length];
        var interim = init;

        for (int i = 0; i < result.Length; i++)
        {
            interim = fct(interim, arr[i]);
            result[i] = interim;
        }

        return result;
    }
*/
    public static long[] OperArray(Func<long, long, long> fct, long[] arr, long init)
    {
        return arr.Reduce(fct, init).ToArray();
    }
}

public static class LinqExtension
{
    public static IEnumerable<long> Reduce(this IEnumerable<long> source, Func<long, long, long> func, long init)
    {
        var aggregate = init;

        foreach (var x in source)
        {
            // init = func(init, x);
            // yield return init;
            aggregate = func(aggregate, x);

            yield return aggregate;
        }
    }
}