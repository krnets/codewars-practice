/*using System.Linq;

public class Kata
{
    public static string Decode(int[] code, int key)
    {
        var keyDigits = key.ToString().Select(char.GetNumericValue).ToArray();
        var longKey = Enumerable.Repeat(keyDigits, code.Length / keyDigits.Length + 1).SelectMany(x => x);

        return string.Concat(code.Zip(longKey, (f, s) => (char) (f + 'a' - s - 1)));
    }
}*/

using System.Linq;

public class Kata
{
    public static string Decode(int[] code, int key)
    {
        // var longKey = string.Concat(Enumerable.Repeat(key.ToString(), code.Length / key.ToString().Length + 1));
        var longKey = Enumerable.Repeat(key.ToString(), code.Length / key.ToString().Length + 1).SelectMany(x => x);

        return string.Concat(code.Zip(longKey, (f, s) => (char) (f - (s - '0') + 'a' - 1)));
    }
}