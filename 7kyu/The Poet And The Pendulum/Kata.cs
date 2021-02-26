/*using System;

public class Kata
{
    public static int[] Pendulum(int[] values)
    {
        var result = new int[values.Length];
        var pos = (values.Length - 1) / 2;
        Array.Sort(values);

        for (int i = 0; i < values.Length; i++)
        {
            if (i % 2 == 0) pos -= i;
            else pos += i;

            result[pos] = values[i];
        }

        return result;
    }
}*/

using System.Linq;

public class Kata
{
    public static int[] Pendulum(int[] values)
    {
        return values.OrderBy(x => x)
            .Aggregate(Enumerable.Empty<int>(), (seq, v) => seq.Count() % 2 == 0 ? seq.Prepend(v) : seq.Append(v))
            .ToArray();
    }
}