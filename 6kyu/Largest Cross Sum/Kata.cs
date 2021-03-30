using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static int LargestCrossSum(int[][] matrix)
    {
        var listOfSums = new List<int>();

        foreach (var row in matrix)
        {
            for (int col = 0; col < row.Length; col++)
            {
                int colSum = matrix.Select((_, i) => matrix[i][col]).Sum();

                listOfSums.Add(row.Sum() + colSum - row[col]);
            }
        }

        return listOfSums.Max();
    }
}