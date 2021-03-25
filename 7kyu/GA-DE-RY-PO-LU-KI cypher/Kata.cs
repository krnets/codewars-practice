using System.Collections.Generic;
using System.Linq;

public class Kata
{
    private static Dictionary<char, char> map = new Dictionary<char, char>();
    private static string keyPairs = "GA-DE-RY-PO-LU-KI";

    static Kata()
    {
        foreach (var pair in keyPairs.Split("-"))
        {
            (char first, char second) = (pair[0], pair[1]);

            map[first] = second;
            map[second] = first;

            (first, second) = (char.ToLower(first), char.ToLower(second));

            map[first] = second;
            map[second] = first;
        }
    }

    public static string Encode(string str) => string.Concat(str.Select(c => map.GetValueOrDefault(c, c)));

    public static string Decode(string str) => Encode(str);
}