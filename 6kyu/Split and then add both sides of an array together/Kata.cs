/*using System.Linq;

public class Kata
{
    public static int[] SplitAndAdd(int[] numbers, int n)
    {
        if (numbers.Length == 1 || n == 0)
            return numbers;

        int[] lastHalf = numbers.Skip(numbers.Length / 2).ToArray();

        for (int i = 0; i < numbers.Length / 2; i++)
            lastHalf[i + numbers.Length % 2] += numbers[i];

        return SplitAndAdd(lastHalf, n - 1);
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static int[] SplitAndAdd(int[] numbers, int n)
    {
        var result = new int[numbers.Length];
        Array.Copy(numbers, result, numbers.Length);

        for (int i = 0; i < n; i++)
        {
            if (result.Length == 1) break;
            if (result.Length % 2 != 0)
                result = new[] {0}.Concat(result).ToArray();

            var half = result.Length / 2;
            result = result.Take(half).Zip(result.Skip(half), (f, s) => f + s).ToArray();
        }

        return result;
    }
}