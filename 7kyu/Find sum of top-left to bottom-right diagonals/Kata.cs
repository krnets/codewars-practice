/*public static class Kata
{
    public static int DiagonalSum(int[,] matrix)
    {
        int sum = 0;

        for (int i = 0; i < matrix.GetLength(0); i++)
            sum += matrix[i, i];

        return sum;
    }
}*/

using System.Linq;

public static class Kata
{
    public static int DiagonalSum(int[,] matrix)
    {
        return Enumerable.Range(0, matrix.GetLength(0)).Sum(i => matrix[i, i]);
    }
}