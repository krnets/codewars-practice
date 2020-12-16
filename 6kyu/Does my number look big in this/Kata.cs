/*using System;
using System.Linq;

public class Kata
{
    public static bool Narcissistic(int value)
    {
        var digits = value.ToString().Select(char.GetNumericValue).ToArray();
        int digitsLength = digits.Length;

        return digits.Select(i => (long) Math.Pow(i, digitsLength)).Sum() == value;
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static bool Narcissistic(int value)
    {
        var digits = value.ToString().Select(char.GetNumericValue).ToArray();

        return digits.Sum(i => (long) Math.Pow(i, digits.Length)) == value;
    }
}