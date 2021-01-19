/*
using System;
using System.Collections.Generic;

namespace Solution
{
    public class Kata
    {
        public static List<Tuple<char, int>> OrderedCount(string input)
        {
            var map = new Dictionary<char, int>();
            var result = new List<Tuple<char, int>>();

            foreach (var c in input)
            {
                if (map.ContainsKey(c))
                    map[c]++;
                else map[c] = 1;
            }

            foreach (var (key, value) in map)
                result.Add(new Tuple<char, int>(key, value));

            return result;
        }
    }
}
*/

using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution
{
    public class Kata
    {
        public static List<Tuple<char, int>> OrderedCount(string input)
        {
            return input.GroupBy(c => c)
                .Select(g => Tuple.Create(g.Key, g.Count()))
                .ToList();
        }
    }

}