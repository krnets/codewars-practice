/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int[][] MatrixAddition(int[][] a, int[][] b)
    {
        var list = new List<List<int>>(a.Length);

        for (int i = 0; i < a.Length; i++)
        {
            var subList = new List<int>();

            for (int j = 0; j < a[0].Length; j++)
                subList.Add(a[i][j] + b[i][j]);

            list.Add(subList);
        }

        return list.Select(sub => sub.ToArray()).ToArray();
    }
}*/

/*public class Kata
{
    public static int[][] MatrixAddition(int[][] a, int[][] b)
    {
        var matrix = new int[a.Length][];

        for (int i = 0; i < a.Length; i++)
        {
            matrix[i] = new int[a.Length];

            for (int j = 0; j < a.Length; j++)
                matrix[i][j] = a[i][j] + b[i][j];
        }

        return matrix;
    }
}*/

using System.Linq;

public class Kata
{
    public static int[][] MatrixAddition(int[][] a, int[][] b)
    {
        // return a.Select((row, i) => row.Select((_, j) => a[i][j] + b[i][j]).ToArray()).ToArray();
        // return a.Select((row, i) => row.Select((x, j) => x + b[i][j]).ToArray()).ToArray();

        return a.Zip(b, (rowA, rowB) =>
                rowA.Zip(rowB, (x, y) => x + y).ToArray())
            .ToArray();
    }
}