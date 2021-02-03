/*using System;
using System.Text;

public class Kata
{
    public static string GetRow(int numOfRow)
    {
        var sb = new StringBuilder();

        if (numOfRow > 26)
            numOfRow = numOfRow % 26;


        for (int i = 0; i < 26; i++)
            sb.Append(i < numOfRow ? Convert.ToChar('A' + numOfRow - 1) : Convert.ToChar('A' + i));

        return sb.ToString();
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static string GetRow(int numOfRow)
    {
        return string.Concat(Enumerable.Range(0, 26)
            .Select(i => (char) (Math.Max(i, (numOfRow - 1) % 26) + 'A')));
    }
}