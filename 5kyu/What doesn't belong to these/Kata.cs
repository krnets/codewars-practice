/*using System.Linq;

public class Kata
{
    public static object FindTheNotFittingElement(object[] series)
    {
        if (series.All(o => o is bool))
            return series.Select(o => (bool) o).Count(b => b) == 1;

        if (series.All(o => o is int))
        {
            var listOfInts = series.Select(o => (int) o).ToList();
            int countPos = 0, countNeg = 0, countOdd = 0, countEven = 0;

            foreach (int i in listOfInts)
            {
                if (i > 0) countPos++;
                if (i < 0) countNeg++;
                if (i % 2 == 0) countEven++;
                if (i % 2 != 0) countOdd++;
            }

            if (countOdd == 1) return listOfInts.Single(x => x % 2 != 0);
            if (countNeg == 1) return listOfInts.Single(x => x < 0);
            if (countPos == 1) return listOfInts.Single(x => x > 0);
            if (countEven == 1) return listOfInts.Single(x => x % 2 == 0);

            return listOfInts.Aggregate((acc, x) => acc ^ x);
        }

        if (series.All(o => o is char))
        {
            var listOfChars = series.Select(o => (char) o).ToList();
            int countUpper = 0, countLower = 0, countNonAlpha = 0, countDigit = 0;

            foreach (char c in listOfChars)
            {
                if (char.IsUpper(c)) countUpper++;
                if (char.IsLower(c)) countLower++;
                if (char.IsDigit(c)) countDigit++;
                if (!char.IsLetterOrDigit(c)) countNonAlpha++;
            }

            if (countDigit == 1) return listOfChars.Single(char.IsDigit);
            if (countLower == 1) return listOfChars.Single(char.IsLower);
            if (countUpper == 1) return listOfChars.Single(char.IsUpper);
            if (countNonAlpha == 1) return listOfChars.Single(c => !char.IsLetter(c));

            return (char) series.Select(o => (int) ((char) o)).Aggregate((acc, x) => acc ^ x);
        }

        var countByType = series.GroupBy(o => o.GetType())
            .ToDictionary(g => g.Key, g => g.Count());

        var uniqueType = countByType.Single(p => p.Value == 1).Key;

        return series.SingleOrDefault(o => o.GetType() == uniqueType);
    }
}*/


using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static object FindTheNotFittingElement(object[] series)
    {
        var rules = new Func<object[], object>[]
        {
            s => s.GroupBy(o => o.GetType()).FirstOrDefault(g => g.Count() == 1)?.Single(), // dif type

            s => s.GroupBy(o => o).Is(c => c.Count() == 2)?.FirstOrDefault(g => g.Count() == 1)?.Single(),

            s => s.Are(i => i is int)?.Cast<int>().GroupBy(i => i % 2).FirstOrDefault(e => e.Count() == 1)?.Single(), // odd or even

            s => s.Are(i => i is int)?.Cast<int>().GroupBy(i => i < 0).FirstOrDefault(e => e.Count() == 1)?.Single(), // < 0 || > 0

            s => s.Are(c => c is char)?.Cast<char>().GroupBy(char.IsLetter).FirstOrDefault(e => e.Count() == 1)?.Single(),

            s => s.Are(c => c is char)?.Cast<char>().GroupBy(char.IsLower).FirstOrDefault(e => e.Count() == 1)?.Single()
        };

        return rules.Select(rule => rule(series)).First(rule => rule != null);
    }
}

internal static class EnumerableExtensions
{
    public static IEnumerable<T> Is<T>(this IEnumerable<T> source, Func<IEnumerable<T>, bool> predicate) => predicate(source) ? source : null;

    public static IEnumerable<T> Are<T>(this IEnumerable<T> source, Func<T, bool> predicate) => source.All(predicate) ? source : null;
}