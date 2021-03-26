using System.Linq;

public class Pattern16
{
    public static string Pattern(int n)
    {
        if (n < 0) return string.Empty;

        var matrix = new int[n][];

        for (int i = 0; i < n; i++)
        {
            matrix[i] = new int[n];

            for (int j = 0; j < n; j++)
                matrix[i][j] = (n - j) % 10;

            for (int j = i; j < n; j++)
                matrix[i][j] = (n - i) % 10;
        }

        return string.Join("\n", matrix.Select(row => string.Concat(row.Select(v => $"{v}"))));
    }
}