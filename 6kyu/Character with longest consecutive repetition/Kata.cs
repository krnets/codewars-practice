using System.Linq;
using System.Text.RegularExpressions;

namespace Solution
{
    using System;

    public static class Kata
    {
        public static Tuple<char?, int> LongestRepetition(string input)
        {
            if (string.IsNullOrEmpty(input))
                return new Tuple<char?, int>(null, 0);

            var groupByLength = Regex.Matches(input, @"(.)(\1*)").Select(m => m.Value).ToList();
            var max = groupByLength.Max(s => s.Length);
            var firstLongest = groupByLength.First(s => s.Length == max);

            return new Tuple<char?, int>(firstLongest[0], firstLongest.Length);
        }
    }
}