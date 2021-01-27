using System.Linq;

public static class Kata
{
    public static int WordsToMarks(string str)
    {
        //return str.Select(c => c - 'a' + 1).Sum();
        return str.Sum(c => c - 'a' + 1);
    }
}