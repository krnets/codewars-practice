using System.Collections.Generic;
using System.Linq;

public partial class Kata
{
    public static string MakeBackronym(string s)
    {
        return string.Join(" ", s.ToUpper().Select(c => dict[c]));
    }

    private static Dictionary<char, string> dict = new()
    {
        {'A', "awesome"},
        {'B', "beautiful"},
        {'C', "confident"},
        {'D', "disturbing"},
        {'E', "eager"},
        {'F', "fantastic"},
        {'G', "gregarious"},
        {'H', "hippy"},
        {'I', "ingestable"},
        {'J', "joke"},
        {'K', "klingon"},
        {'L', "literal"},
        {'M', "mustache"},
        {'N', "newtonian"},
        {'O', "oscillating"},
        {'P', "perfect"},
        {'Q', "queen"},
        {'R', "rant"},
        {'S', "stylish"},
        {'T', "turn"},
        {'U', "underlying"},
        {'V', "volcano"},
        {'W', "weird"},
        {'X', "xylophone"},
        {'Y', "yogic"},
        {'Z', "zero"}
    };
}