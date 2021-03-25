using System.Collections.Generic;
using System.Linq;

public class Kata
{
    private static string[] possibleKeys =
    {
        "GA-DE-RY-PO-LU-KI",
        "PO-LI-TY-KA-RE-NU",
        "KA-CE-MI-NU-TO-WY",
        "KO-NI-EC-MA-TU-RY",
        "ZA-RE-WY-BU-HO-KI",
        "BA-WO-LE-TY-KI-JU",
        "RE-GU-LA-MI-NO-WY"
    };

    public static string SearchForKey(string[] messages, string[] secrets)
    {
        foreach (var key in possibleKeys)
            foreach (var secret in secrets)
                if (messages[0] == Decode(secret, key))
                    return string.Concat(key.ToLower().Split("-")
                        .Select(s => string.Concat(s.OrderBy(c => c)))
                        .OrderBy(s => s));

        return "noidea";
    }

    public static string Decode(string str, string key)
    {
        var map = new Dictionary<char, char>();

        foreach (var pair in key.ToLower().Split("-"))
        {
            (char first, char second) = (pair[0], pair[1]);
            map[first] = second;
            map[second] = first;
        }

        return string.Concat(str.Select(c => map.GetValueOrDefault(c, c)));
    }
}