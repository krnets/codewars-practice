/*using System;
using System.Linq;

public class Kata
{
    public static string Change(string input)
    {
        var lettersOnly = input.ToLower().Where(char.IsLetter).ToList();
        //var lettersOnly = input.ToLower().Where(char.IsLetter).ToHashSet();

        return string.Concat(Enumerable.Range(0, 26)
            .Select(i => lettersOnly.Contains(Convert.ToChar('a' + i)) ? 1 : 0));
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static string Change(string input)
    {
        int n = input.Where(char.IsLetter).Aggregate(0, (a, b) => a | (1 << 26 - b % 32));

        return Convert.ToString(n, 2).PadLeft(26, '0');
    }
}