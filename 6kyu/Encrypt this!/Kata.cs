/*
using System.Collections.Generic;
using System.Text;

namespace EncryptThis
{
    public class Kata
    {
        public static string EncryptThis(string input)
        {
            if (string.IsNullOrEmpty(input))
                return string.Empty;

            var words = input.Split();
            var result = new List<string>();

            foreach (var word in words)
            {
                int firstCharToInt = word[0];
                var sb = new StringBuilder().Append(firstCharToInt);

                if (word.Length > 1)
                {
                    char secondLetter = word[1];

                    if (word.Length > 2)
                    {
                        char lastLetter = word[^1];
                        string middlePart = word[2..^1];
                        sb.Append(lastLetter).Append(middlePart);
                    }

                    sb.Append(secondLetter);
                }

                result.Add(sb.ToString());
            }

            return string.Join(" ", result);
        }
    }
}
*/

/*using System.Linq;
using System.Text.RegularExpressions;

namespace EncryptThis
{
    public class Kata
    {
        public static string EncryptThis(string input)
        {
            return string.Join(" ", input.Split()
                .Where(str => str.Length > 0)
                .Select(str => $"{(int) str[0]}{Regex.Replace(str[1..], "(.)(.*)(.)", "$3$2$1")}"));
        }
    }
}*/

using System.Collections.Generic;

namespace EncryptThis
{
    public class Kata
    {
        public static string EncryptThis(string input)
        {
            if (string.IsNullOrEmpty(input))
                return string.Empty;

            var result = new List<string>();

            foreach (var word in input.Split())
            {
                switch (word.Length)
                {
                    case 1: result.Add($"{(int) word[0]}"); break;
                    case 2: result.Add($"{(int) word[0]}{word[1]}"); break;
                    default: result.Add($"{(int) word[0]}{word[^1]}{word[2..^1]}{word[1]}"); break;
                }
            }

            return string.Join(" ", result);
        }
    }
}