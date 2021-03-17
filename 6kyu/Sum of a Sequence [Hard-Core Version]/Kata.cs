using System;

public static class Kata
{
    public static long SequenceSum(long start, long end, long step)
    {
        if (Math.Sign(end - start) != Math.Sign(step))
            return 0;

        var n = (end - start) / step;

        return (n + 1) * (n * step + 2 * start) / 2;
    }
}