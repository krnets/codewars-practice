using System.Linq;

public class Kata
{
    public static int DontGiveMeFive(int start, int end)
    {
        return Enumerable
            .Range(start, end - start + 1)
            .Count(n => !n.ToString().Contains('5'));
            // .Count(n => !n.ToString().Contains("5"));
    }
}