public class TheClockwiseSpiral
{
    public static int[,] CreateSpiral(int N)
    {
        var matrix = new int[N, N];
        int count = 1;
        int nSquared = N * N;

        int rowStart = 0, colStart = 0;
        int rowEnd = N - 1, colEnd = N - 1;

        while (count <= nSquared)
        {
            for (int j = colStart; j <= colEnd; j++)
                matrix[rowStart, j] = count++;

            rowStart++;

            for (int i = rowStart; i <= rowEnd; i++)
                matrix[i, colEnd] = count++;

            colEnd--;

            for (int j = colEnd; j >= colStart; j--)
                matrix[rowEnd, j] = count++;

            rowEnd--;

            for (int i = rowEnd; i >= rowStart; i--)
                matrix[i, colStart] = count++;

            colStart++;
        }

        return matrix;
    }
}