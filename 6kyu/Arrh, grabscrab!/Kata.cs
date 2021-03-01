using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static List<string> Grabscrab(string anagram, List<string> dictionary)
    {
        return dictionary.Where(w => w.OrderBy(c => c).SequenceEqual(anagram.OrderBy(c => c))).ToList();
    }
}