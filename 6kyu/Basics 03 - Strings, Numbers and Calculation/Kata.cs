/*namespace smile67Kata
{
    using System;
    using System.Linq;
    using System.Text.RegularExpressions;

    public class Kata
    {
        public string calculateString(string calcIt)
        {
            var op = Regex.Match(calcIt, @"[+\-#1#]").Value;
            var splitIndex = op.Length > 0 ? calcIt.IndexOf(op) : 0;
            var left = double.Parse(string.Concat(calcIt.Substring(0, splitIndex)
                .Where(c => char.IsDigit(c) || c == '.')));
            var right = double.Parse(string.Concat(calcIt.Substring(splitIndex)
                .Where(c => char.IsDigit(c) || c == '.')));

            var result = op is "+" ? left + right :
                op is "-" ? left - right :
                op is "*" ? left * right :
                op is "/" ? left / right : 0;

            return Math.Round(result).ToString();
        }
    }
}*/

using System;
using System.Data;
using System.Linq;
using System.Text.RegularExpressions;

namespace smile67Kata
{
    public class Kata
    {
        public string calculateString(string calcIt)
        {
            var expression = string.Concat(Regex.Matches(calcIt, @"[+\-*/.\d]+").Select(m => m.Value));
            var result = Convert.ToDouble(new DataTable().Compute(expression, null));

            return Math.Round(result).ToString();
        }
    }
}