using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public int SquareDigitsSequence(int a0)
    {
        var nums = new HashSet<double>();
        double d = a0;

        while (!nums.Contains(d))
        {
            nums.Add(d);
            d = $"{d}".Sum(c => Math.Pow(char.GetNumericValue(c), 2));
        }

        return nums.Count + 1;
    }
}