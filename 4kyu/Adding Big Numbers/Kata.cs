/*using System.Numerics;

public class Kata
{
    public static string Add(string a, string b)
    {
        return (BigInteger.Parse(a) + BigInteger.Parse(b)).ToString();
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static string Add(string a, string b)
    {
        int maxLength = Math.Max(a.Length, b.Length);
        var intsA = a.PadLeft(maxLength, '0').Select(c => (int) char.GetNumericValue(c)).ToArray();
        var intsB = b.PadLeft(maxLength, '0').Select(c => (int) char.GetNumericValue(c)).ToArray();

        var result = string.Empty;
        int carry = 0, sum;

        for (int i = maxLength - 1; i >= 0; i--)
        {
            sum = intsA[i] + intsB[i] + carry;
            carry = sum / 10;
            result = sum % 10 + result;
        }

        return (carry == 1 ? "1" : string.Empty) + result;
    }
}