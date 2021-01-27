/*public class Kata
{
    public static double[] Averages(int[] numbers)
    {
        if (numbers == null || numbers.Length < 2)
            return new double[0];

        var result = new double[numbers.Length - 1];

        for (int i = 0; i < numbers.Length - 1; i++)
            result[i] = (numbers[i] + numbers[i + 1]) / 2.0;

        return result;
    }
}*/

using System.Linq;

public class Kata
{
    public static double[] Averages(int[] numbers)
    {
        return numbers?.Zip(numbers.Skip(1), (x, y) => (x + y) / 2.0).ToArray() ?? new double[0];
    }
}