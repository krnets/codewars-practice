/*using System.Collections.Generic;
using System.Linq;

class Kata
{
    public static int SequenceClassifier(int[] arr)
    {
        var classes = new Dictionary<string, int>
        {
            ["unordered"] = 0,
            ["strictly increasing"] = 1,
            ["not decreasing"] = 2,
            ["strictly decreasing"] = 3,
            ["not increasing"] = 4,
            ["constant"] = 5
        };

        if (arr.Distinct().Count() == 1)
            return classes["constant"];

        if (arr.Zip(arr.Skip(1), (a, b) => b - a > 0).All(b => b))
            return classes["strictly increasing"];

        if (arr.Zip(arr.Skip(1), (a, b) => b - a >= 0).All(b => b))
            return classes["not decreasing"];

        if (arr.Zip(arr.Skip(1), (a, b) => a - b > 0).All(b => b))
            return classes["strictly decreasing"];

        if (arr.Zip(arr.Skip(1), (a, b) => a - b >= 0).All(b => b))
            return classes["not increasing"];

        return classes["unordered"];
    }
}*/

using System.Linq;

class Kata
{
    public static int SequenceClassifier(int[] arr)
    {
        int[] diffs = arr.Zip(arr.Skip(1), (a, b) => b - a).ToArray();
        int sum = diffs.Sum();
        int len = arr.Length - 1;
        bool containsZero = diffs.Contains(0);
        bool allNegative = diffs.All(x => x < 0);
        bool anyNegative = diffs.Any(x => x < 0);
        bool anyPositive = diffs.Any(x => x > 0);

        return sum == 0 && !anyNegative ? 5
            : !anyPositive && containsZero ? 4
            : allNegative && -sum >= len ? 3
            : containsZero && !allNegative && !anyNegative ? 2
            : !containsZero && sum >= len ? 1
            : 0;
    }
}