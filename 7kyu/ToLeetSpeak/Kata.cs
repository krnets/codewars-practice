/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string ToLeetSpeak(string str)
    {
        var leetDictionary = new Dictionary<char, char>
        {
            {'A', '@'}, {'B', '8'}, {'C', '('}, {'E', '3'}, {'G', '6'}, {'H', '#'},
            {'I', '!'}, {'L', '1'}, {'O', '0'}, {'S', '$'}, {'T', '7'}, {'Z', '2'}
        };

        return string.Concat(str.Select(c => leetDictionary.ContainsKey(c) ? leetDictionary[c] : c));
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string ToLeetSpeak(string str)
    {
        var leetDictionary = new Dictionary<char, char>
        {
            ['A'] = '@', ['B'] = '8', ['C'] = '(', ['E'] = '3', ['G'] = '6', ['H'] = '#',
            ['I'] = '!', ['L'] = '1', ['O'] = '0', ['S'] = '$', ['T'] = '7', ['Z'] = '2'
        };

        return string.Concat(str.Select(c => leetDictionary.GetValueOrDefault(c, c)));
    }
}