/*using System;
using System.Collections.Generic;

public class FizzBuzz
{
    public static string[] GetFizzBuzzArray(int n)
    {
        if (n == 0) throw new ArgumentOutOfRangeException();

        var list = new List<string>();

        for (int i = 1; i <= n; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
                list.Add("FizzBuzz");
            else if (i % 3 == 0)
                list.Add("Fizz");
            else if (i % 5 == 0)
                list.Add("Buzz");
            else list.Add(i.ToString());
        }

        return list.ToArray();
    }
}*/

using System;
using System.Linq;

public class FizzBuzz
{
    public static string[] GetFizzBuzzArray(int n)
    {
        return n > 0 ? Enumerable.Range(1, n)
            .Select(i => i % 3 == 0 && i % 5 == 0 ? "FizzBuzz" : i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : i.ToString())
            .ToArray() :
            throw new ArgumentOutOfRangeException();
    }
}