/*using System.Linq;

public class Kata
{
    public static int GetLengthOfMissingArray(object[][] arrayOfArrays)
    {
        if (arrayOfArrays == null || arrayOfArrays.Length == 0 ||
            arrayOfArrays.Any(arr => arr == null || arr.Length == 0))
            return 0;

        var lengths = arrayOfArrays.Select(arr => arr.Length).ToArray();
        var min = lengths.Min();
        var max = lengths.Max();

        return Enumerable.Range(min, max - min).Except(lengths).First();
    }
}*/

using System.Linq;

public static class Kata
{
    public static int GetLengthOfMissingArray(object[][] arrayOfArrays)
    {
        if (arrayOfArrays.IsNullOrEmpty() || arrayOfArrays.Any(IsNullOrEmpty))
            return 0;

        var lengths = arrayOfArrays.Select(arr => arr.Length).ToArray();

        return Enumerable.Range(lengths.Min(), lengths.Length).Except(lengths).First();
    }

    private static bool IsNullOrEmpty(this object[] array) => array == null || array.Length == 0;
}