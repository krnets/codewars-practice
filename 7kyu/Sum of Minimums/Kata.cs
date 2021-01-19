/*
using System;

class Kata
{
    public static int SumOfMinimums(int[,] numbers)
    {
        double sum = 0;

        for (int i = 0; i < numbers.GetLength(0); i++)
        {
            var min = double.MaxValue;

            for (int j = 0; j < numbers.GetLength(1); j++)
                min = Math.Min(min, numbers[i, j]);

            sum += min;
        }

        return (int)sum;
    }
}
*/

using System.Linq;

class Kata
{
    public static int SumOfMinimums(int[,] numbers)
    {
        return Enumerable.Range(0, numbers.GetLength(0))
            .Select(i => Enumerable.Range(0, numbers.GetLength(1))
                .Select(j => numbers[i, j]))
            .Sum(x => x.Min());
    }
}