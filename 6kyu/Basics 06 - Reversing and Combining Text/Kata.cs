/*namespace smile67Kata
{
    using System.Collections.Generic;
    using System.Linq;

    public class Kata
    {
        public string reverseAndCombineText(string text)
        {
            var words = text.Split().ToList();

            while (words.Count > 1)
            {
                words = words.Select(w => string.Concat(w.Reverse())).ToList();
                var list = new List<string>();

                for (int i = 0; i < words.Count; i += 2)
                {
                    if (i == words.Count - 1)
                    {
                        list.Add(words[i]);
                        break;
                    }

                    list.Add(words[i] + words[i + 1]);
                }

                words = list;
            }

            return words[0];
        }
    }
}*/


namespace smile67Kata
{
    using System.Linq;

    public class Kata
    {
        public string reverseAndCombineText(string text)
        {
            var words = text.Split();

            while (words.Length > 1)
                words = words.Select((w, i) => new {reversedWord = string.Concat(w.Reverse()), index = i})
                    .GroupBy(obj => obj.index / 2)
                    .Select(g => string.Concat(g.Select(obj => obj.reversedWord))).ToArray();

            return words[0];
        }
    }
}