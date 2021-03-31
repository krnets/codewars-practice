using System.Linq;
using System.Text;

public class Kata
{
    public static string Encode(string message, string key, int initShift) => CondiHelper(message, key, initShift, true);

    public static string Decode(string message, string key, int initShift) => CondiHelper(message, key, initShift, false);

    private static string CondiHelper(string message, string key, int initShift, bool forward)
    {
        var keyDistinct = key.Distinct().ToList();
        var alphabet = Enumerable.Range('a', 26).Select(i => (char) i);
        var abcNotInKey = alphabet.Except(keyDistinct);
        var condiKey = keyDistinct.Concat(abcNotInKey).Take(26).ToList();
        var shiftPos = initShift % 26;
        var sb = new StringBuilder();

        foreach (char c in message)
        {
            if (char.IsLetter(c))
            {
                var prev = condiKey.IndexOf(c);
                char cEncoded;

                if (forward)
                {
                    cEncoded = condiKey[(26 + prev + shiftPos) % 26];
                    shiftPos = (prev + 1) % 26;
                }
                else
                {
                    cEncoded = condiKey[(26 + prev - shiftPos) % 26];
                    shiftPos = (26 + prev + 1 - shiftPos) % 26;
                }

                sb.Append(cEncoded);
            }
            else sb.Append(c);
        }

        return sb.ToString();
    }
}