using System.Linq;
using System.Text;

class CaesarCrypto
{
    public static string Encode(string text, int shift)
    {
        if (string.IsNullOrEmpty(text) || text.Replace(" ", "").Length == 0)
            return string.Empty;

        var abcLower = Enumerable.Range('a', 26).Select(i => (char) i);
        var abcUpper = Enumerable.Range('A', 26).Select(i => (char) i);
        var alphabet = abcLower.Concat(abcUpper).ToList();
        var sb = new StringBuilder();

        foreach (char c in text)
            if (char.IsLetter(c))
            {
                int i = (alphabet.IndexOf(c) + shift) % alphabet.Count;

                sb.Append(i < 0 ? alphabet[alphabet.Count + i] : alphabet[i]);
            }
            else sb.Append(c);

        return sb.ToString();
    }
}