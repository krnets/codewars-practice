/*using System.Linq;
using System.Text.RegularExpressions;

namespace myjinxin
{
    using System;

    public class Kata
    {
        public int SwapAdjacentBits(int n)
        {
            var binary = Convert.ToString(n, 2);
            binary = (binary.Length % 2 == 0 ? "" : "0") + binary;

            var pairBits = Regex.Split(binary, "(?<=\\G.{2})")
                .Select(pair => string.Concat(pair.Reverse()));

            return Convert.ToInt32(string.Concat(pairBits), 2);
        }
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

namespace myjinxin
{
    using System;

    public class Kata
    {
        public int SwapAdjacentBits(int n)
        {
            var binary = Convert.ToString(n, 2).PadLeft(32, '0');

            var pairBits = Regex.Split(binary, "(?<=\\G.{2})")
                .Select(pair => string.Concat(pair.Reverse()));

            return Convert.ToInt32(string.Concat(pairBits), 2);
        }
    }
}