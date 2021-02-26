using System.Linq;

public class Kata
{
    public static bool IsNice(int[] arr)
    {
        // return arr.Length > 0 && arr.All(x => arr.Contains(x - 1) || arr.Contains(x + 1));
        return arr.Any() && arr.All(x => arr.Contains(x - 1) || arr.Contains(x + 1));
    }
}