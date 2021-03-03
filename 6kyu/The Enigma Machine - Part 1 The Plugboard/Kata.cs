using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Plugboard
{
    private Dictionary<char, char> map = new Dictionary<char, char>();

    public Plugboard(string wires = "")
    {
        var pairs = Regex.Split(wires, @"(?<=\G.{2})")
            .Where(x => x.Length > 0).ToArray();

        if (pairs.Length > 10 || pairs.Any(p => p.Length == 1) || wires.Distinct().Count() != wires.Length)
            throw new SystemException();

        foreach (var pair in pairs)
        {
            var firstChar = pair[0];
            var secondChar = pair[1];

            map[firstChar] = secondChar;
            map[secondChar] = firstChar;
        }
    }

    public char process(char c)
    {
        return map.GetValueOrDefault(c, c);
    }
}