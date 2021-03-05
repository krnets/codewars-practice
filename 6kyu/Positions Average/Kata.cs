/*using System.Linq;

public class PositionAverage
{
    public static double PosAverage(string s)
    {
        var nums = s.Split(", ");
        var common = 0d;
        var totals = nums.Length * (nums.Length - 1) / 2d;

        for (int i = 0; i < nums.Length - 1; i++)
            for (int j = i + 1; j < nums.Length; j++)
                common += nums[i].Zip(nums[j], (x, y) => x == y).Count(m => m);

        return 100.0 * common / nums[0].Length / totals;
    }
}*/

using System.Linq;

public class PositionAverage
{
    public static double PosAverage(string s)
    {
        var nums = s.Split(", ");

        var common = nums
            .SelectMany((x, i) => nums.Skip(i + 1)
                .SelectMany(y => x.Zip(y, (a, b) => a == b)))
            .ToArray();

        return 100.0 * common.Count(m => m) / common.Length;
    }
}