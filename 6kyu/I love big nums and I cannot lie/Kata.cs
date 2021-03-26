using System.Linq;

public class Kata
{
    public static string Biggest(int[] nums)
    {
        return nums.Max() == 0 ? "0" : string.Concat(nums.Select(n => $"{n}").OrderByDescending(s => s + s));
    }
}