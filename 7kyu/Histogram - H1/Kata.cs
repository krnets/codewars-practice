/*using System.Collections.Generic;

public class Dinglemouse
{
    public static string Histogram(int[] results)
    {
        var list = new LinkedList<string>();

        for (int i = 0; i < results.Length; i++)
        {
            var count = results[i];
            var hashes = new string('#', count);
            var sub = count > 0 ? $"{hashes} {count}" : null;
            var str = $"{i + 1}|{sub}\n";
            list.AddFirst(str);
        }

        return string.Join("", list);
    }
}*/

using System.Linq;

public class Dinglemouse
{
    public static string Histogram(int[] results)
    {
        return string.Concat(results
            .Select((freq, i) => $"{i + 1}|{new string('#', freq)}{(freq > 0 ? $" {freq}" : string.Empty)}\n")
            .Reverse());
    }
}