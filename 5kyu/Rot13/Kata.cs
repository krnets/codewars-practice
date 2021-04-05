using System.Linq;
using static System.Char;

public class Kata
{
    public static string Rot13(string message)
    {
        return string.Concat(message.Select(c => (char) (IsLetter(c) ? IsUpper(c) ? (c - 'A' + 13) % 26 + 'A' : (c - 'a' + 13) % 26 + 'a' : c)));
    }
}