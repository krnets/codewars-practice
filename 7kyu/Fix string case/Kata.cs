/*class Kata
{
    public static string Solve(string s)
    {
        int countCaps = 0;
        int halfLength = s.Length / 2;
        bool toAllCapps = false;

        foreach (char c in s)
        {
            if (char.IsUpper(c)) countCaps++;

            if (countCaps > halfLength)
            {
                toAllCapps = true;
                break;
            }
        }

        return toAllCapps ? s.ToUpper() : s.ToLower();
    }
}*/
using System.Linq;

class Kata
{
    public static string Solve(string s)
    {
        return s.Count(char.IsUpper) > s.Length / 2 ? s.ToUpper() : s.ToLower();
    }
}