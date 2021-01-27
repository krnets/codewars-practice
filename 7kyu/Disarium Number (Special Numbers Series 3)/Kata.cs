/*using System;
using System.Linq;

class Kata
{
    public static string DisariumNumber(int number)
    {
        var digits = number.ToString().Select(char.GetNumericValue).ToArray();

        return Enumerable.Range(0, digits.Length)
            .Sum(i => Math.Pow(digits[i], (i + 1))) == number
            ? "Disarium !!"
            : "Not !!";
    }
}*/

using System;
using System.Linq;

class Kata
{
    public static string DisariumNumber(int number)
    {
        return number.ToString().Select((c, i) => Math.Pow(char.GetNumericValue(c), i + 1)).Sum() == number
            ? "Disarium !!"
            : "Not !!";
    }
}