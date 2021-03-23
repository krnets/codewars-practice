using System.Linq;

public class Pattern12
{
    public static string Pattern(int n)
    {
        if (n < 1) return string.Empty;

        var length = 2 * n - 1;
        var mid = length / 2;
        var result = new char[length][];

        for (int i = 0; i < length; i++)
            result[i] = Enumerable.Repeat(' ', length).ToArray();

        for (int i = 0; i < length; i++)
        {
            char c = (char) ((i < mid ? i + 1 : length - i) % 10 + '0');
            result[i][i] = c;
            result[length - i - 1][i] = c;
        }

        return string.Join("\n", result.Select(row => string.Concat(row)));
    }
}