using System.Linq;

public class Dinglemouse
{
    public static string Histogram(int[] results)
    {
        int sum = results.Sum();

        return string.Concat(results.Select((freq, i) =>
                $"{i + 1}|" +
                $"{(freq > 0 ? $"{new string('\u2588', freq * 50 / sum)} {freq * 100 / sum}%" : string.Empty)}\n")
            .Reverse());
    }
}