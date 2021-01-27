using System.Linq;

public class Kata
{
    public static int[] WordValue(string[] a)
    {
        return a.Select((word, index) => word.Where(char.IsLetter)
                .Sum(c => c - 'a' + 1) * (index + 1))
            .ToArray();
    }
}