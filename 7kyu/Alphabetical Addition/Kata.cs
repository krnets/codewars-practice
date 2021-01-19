using System.Linq;

public class Kata
{
    public static char AddLetters(char[] letters)
    {
        if (letters.Length == 0) return 'z';

        return (char)((letters.Sum(ch => ch - 'a' + 1) - 1) % 26 + 'a');
    }
}