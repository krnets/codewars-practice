using System;
using System.Linq;

class Kata
{
    public static string JumpingNumber(int number)
    {
        var digits = number.ToString().Select(char.GetNumericValue).ToList();

        return number < 10 || digits.Zip(digits.Skip(1))
            .All(t => Math.Abs(t.Second - t.First) == 1)
            ? "Jumping!!"
            : "Not!!";
    }
}