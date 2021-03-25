/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string FindTheKey(string[] messages, string[] secrets)
    {
        var keys = new HashSet<string>();

        for (int i = 0; i < messages.Length; i++)
        {
            for (int c = 0; c < messages[i].Length; c++)
            {
                if (messages[i][c] != secrets[i][c])
                {
                    var m = messages[i][c];
                    var s = secrets[i][c];
                    var key = string.Concat($"{m}{s}".OrderBy(a => a));

                    keys.Add(key);
                }
            }
        }

        return string.Concat(keys.OrderBy(k => k));
    }
}*/

using System.Linq;

public class Kata
{
    public static string FindTheKey(string[] messages, string[] secrets)
    {
        return string.Concat(string.Concat(messages)
            .Zip(string.Concat(secrets), (m, s) => (m < s ? $"{m}{s}" : $"{s}{m}"))
            .Distinct()
            .Where(s => s[0] != s[1])
            .OrderBy(s => s));
    }
}