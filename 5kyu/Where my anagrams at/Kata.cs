using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static List<string> Anagrams(string word, List<string> words)
    {
        var compareWord = word.OrderBy(c => c);

        return words.FindAll(w => w.OrderBy(c => c).SequenceEqual(compareWord));
    }
}