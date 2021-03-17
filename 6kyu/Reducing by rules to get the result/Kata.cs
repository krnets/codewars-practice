/*using System;
using System.Linq;

public class Kata
{
    public static double ReduceByRules(double[] numbers, Func<double, double, double>[] rules)
    {
        int index = 0;

        return numbers.Aggregate((x, y) => rules[index++ % rules.Length](x, y));
    }
}*/

using System;

public class Kata
{
    public static double ReduceByRules(double[] numbers, Func<double, double, double>[] rules)
    {
        double acc = numbers[0];

        for (int i = 0; i < numbers.Length - 1; i++)
            // acc = rules[i % rules.Length](acc, numbers[i + 1]);
            acc = rules[i % rules.Length].Invoke(acc, numbers[i + 1]);

        return acc;
    }
}

/*using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static double ReduceByRules(double[] numbers, Func<double, double, double>[] rules)
    {
        return numbers.Skip(1)
            .Zip(Cycle(rules), (d, rule) => new {x = d, rule})
            .Aggregate(numbers.First(), (acc, next) => next.rule(acc, next.x));
    }

    private static IEnumerable<T> Cycle<T>(this IEnumerable<T> list)
    {
        // for (;;)
        while (true)
            foreach (T t in list)
                yield return t;
    }
}*/