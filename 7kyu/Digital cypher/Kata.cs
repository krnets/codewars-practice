/*using System.Linq;

public class Kata
{
    public static int[] Encode(string str, int n)
    {
        var keyDigits = n.ToString().Select(c => (int) char.GetNumericValue(c)).ToArray();

        return str.Select((ch, i) => ch - 'a' + keyDigits[i % keyDigits.Length] + 1).ToArray();
    }
}*/

using System.Linq;

public class Kata
{
    public static int[] Encode(string str, int n)
    {
        var key = n.ToString().Select(x => x - '0').ToArray();
        var longKey = Enumerable.Repeat(key, str.Length / key.Count() + 1).SelectMany(x => x).ToArray();

        return str.Zip(longKey, (f, s) => f - 'a' + s + 1).ToArray();
    }
}