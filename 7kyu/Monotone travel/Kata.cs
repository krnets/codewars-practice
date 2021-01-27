using System.Linq;

public class Kata
{
    public static bool IsMonotone(int[] arr)
    {
        return arr.Zip(arr.Skip(1)).All((tuple => tuple.Second - tuple.First >= 0));
    }
}

/*using System.Linq;

public class Kata
{
    public static bool IsMonotone(int[] arr)
    {
        return arr.OrderBy(i => i).SequenceEqual(arr);
    }
}*/

/*using System.Linq;

public class Kata
{
    public static bool IsMonotone(int[] arr)
    {
        return arr.Skip(1).Select((x, i) => x >= arr[i]).All(b => b);
    }
}*/