using System.Linq;
using static System.String;

public static class Kata
{
    public static string ReverseWords(string str)
    {
        return Join(' ', str.Split().Select(word => Concat(word.Reverse())));
    }
}