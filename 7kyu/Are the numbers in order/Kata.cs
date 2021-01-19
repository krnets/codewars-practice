/*public class Kata
{
    public static bool IsAscOrder(int[] arr)
    {
        for (int i = 1; i < arr.Length; i++)
            if (arr[i] < arr[i - 1])
                return false;

        return true;
    }
}*/

using System.Linq; 

public class Kata
{
    public static bool IsAscOrder(int[] arr)
    {
        return arr.OrderBy(x => x).SequenceEqual(arr);
    }
}