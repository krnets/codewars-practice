/*public class Kata
{
    public static string CreatePhoneNumber(int[] numbers)
    {
        int[] nums = numbers;

        return string.Format(
            $"({nums[0]}{nums[1]}{nums[2]}) {nums[3]}{nums[4]}{nums[5]}-{nums[6]}{nums[7]}{nums[8]}{nums[9]}",
            numbers);
    }
}*/

/*using System;
using System.Linq;

public class Kata
{
    public static string CreatePhoneNumber(int[] numbers)
    {
        return String.Format("({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}", numbers.Select(x => x.ToString()).ToArray());
    }
}*/

public class Kata
{
    public static string CreatePhoneNumber(int[] numbers)
    {
        // return $"{long.Parse(string.Concat(numbers)):(000) 000-0000}";
        return long.Parse(string.Concat(numbers)).ToString("(000) 000-0000");
    }
}