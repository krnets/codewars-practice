/*public class Kata
{
    public static int[,] MatrixMultiplication(int[,] a, int[,] b)
    {
        var c = new int[a.GetLength(0), a.GetLength(1)];

        for (int i = 0; i < a.GetLength(0); i++)
        {
            for (int j = 0; j < a.GetLength(1); j++)
            {
                for (int k = 0; k < a.GetLength(1); k++)
                {
                    c[i, j] += a[i, k] * b[k, j];
                }
            }
        }

        return c;
    }
}*/

public class Kata
{
    public static int[,] MatrixMultiplication(int[,] a, int[,] b)
    {
        var n = a.GetLength(0);
        var c = new int[n, n];

        for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        for (int k = 0; k < n; k++)
            c[i, j] += a[i, k] * b[k, j];

        return c;
    }
}