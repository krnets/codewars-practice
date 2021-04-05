/*using System;
using System.Linq;

public static class Kata
{
    public static int MaxGap(int[] numbers)
    {
        Array.Sort(numbers);

        return Enumerable.Range(1, numbers.Length - 1)
            .Select(i => Math.Abs(numbers[i] - numbers[i - 1]))
            .Max();
    }
}*/

using System;
using System.Linq;

public static class Kata
{
    public static int MaxGap(int[] numbers)
    {
        Array.Sort(numbers);
        return numbers.Zip(numbers.Skip(1), (a, b) => b - a).Max();
    }
}