/*using System;
using System.Linq;

public static class Kata
{
    public static Func<int, int> GetFunction(int[] sequence)
    {
        int m = sequence[0];
        int n = sequence[1] - m;

        if (sequence.Select((x, i) => x != n * i + m).Any(b => b))
            throw new ArgumentException("Non-linear sequence");

        return x => n * x + sequence[0];
    }
}*/

using System;
using System.Linq;

public static class Kata
{
    public static Func<int, int> GetFunction(int[] sequence)
    {
        int first = sequence[0];
        int step = sequence[1] - first;

        if (sequence.Zip(sequence.Skip(1), (a, b) => b - a).Any(x => x != step))
            throw new ArgumentException("Non-linear sequence");

        return x => step * x + first;
    }
}