/*
public class Kata
{
    public static int CountInversions(int[] array)
    {
        int count = 0;

        for (int i = 0; i < array.Length; i++)
            for (int j = 0; j < i; j++)
                if (array[j] > array[i])
                    count++;

        return count;
    }
}
*/

using System.Linq;

public class Kata
{
    public static int CountInversions(int[] array)
    {
        return array.Select((left, i) => array.Skip(i + 1).Count(right => left > right)).Sum();
    }
}