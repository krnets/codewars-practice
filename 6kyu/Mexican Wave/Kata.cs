/*using System.Collections.Generic;

namespace CodeWars
{
    public class Kata
    {
        public List<string> wave(string str)
        {
            var list = new List<string>();

            for (int i = 0; i < str.Length; i++)
            {
                var charArray = str.ToCharArray();

                if (!char.IsLetter(charArray[i]))
                    continue;

                charArray[i] = char.ToUpper(charArray[i]);
                list.Add(string.Concat(charArray));
            }

            return list;
        }
    }
}*/

using System.Collections.Generic;
using System.Linq;

namespace CodeWars
{
    public class Kata
    {
        public List<string> wave(string str)
        {
            return str
                .Select((c, i) => str[..i] + char.ToUpper(c) + str[(i + 1)..])
                .Where(x => x != str)
                .ToList();
        }
    }
}