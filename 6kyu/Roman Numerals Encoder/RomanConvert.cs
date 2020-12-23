/*using System.Text;

public class RomanConvert
{
    public static string Solution(int n)
    {
        var roman = new[] {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        var nums = new[] {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        var sb = new StringBuilder();

        for (var i = 0; i < nums.Length; i++)
        {
            int num = nums[i];

            while ((n - num) >= 0)
            {
                sb.Append(roman[i]);
                n -= num;
            }
        }

        return sb.ToString();
    }
}*/

/*using System.Collections.Generic;
using System.Text;

public class RomanConvert
{
    public static string Solution(int n)
    {
        var romanNums = new Dictionary<int, string>()
        {
            {1000, "M"},
            {900, "CM"},
            {500, "D"},
            {400, "CD"},
            {100, "C"},
            {90, "XC"},
            {50, "L"},
            {40, "XL"},
            {10, "X"},
            {9, "IX"},
            {5, "V"},
            {4, "IV"},
            {1, "I"}
        };

        var sb = new StringBuilder();

        foreach (var (key, value) in romanNums)
        {
            while ((n - key) >= 0)
            {
                sb.Append(value);
                n -= key;
            }
        }

        return sb.ToString();
    }
}*/

using System.Text;

public class RomanConvert
{
    public static string Solution(int n)
    {
        var thousand = new[] {"", "M", "MM", "MMM"};
        var hundred = new[] {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        var ten = new[] {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        var one = new[] {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

        return new StringBuilder()
            .Append(thousand[n / 1000 % 10])
            .Append(hundred[n / 100 % 10])
            .Append(ten[n / 10 % 10])
            .Append(one[n % 10]).ToString();
    }
}