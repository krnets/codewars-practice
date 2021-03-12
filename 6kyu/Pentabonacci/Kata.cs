using System;

public class Pentanacci
{
    public static long CountOddPentaFib(long n)
    {
        long count = 1;
        var array = new long[n + 1];
        var initial = new[] {0, 1, 1, 2, 4};
        var length = initial.Length;
        Array.Copy(initial, array, length);

        for (int i = length; i <= n; i++)
        {
            for (int j = 1; j <= length; j++)
                array[i] += array[i - j];

            if (array[i] % 2 != 0)
                count++;
        }

        return count;
    }
}