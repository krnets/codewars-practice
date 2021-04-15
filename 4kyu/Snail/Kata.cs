using System.Linq;

public class SnailSolution
{
    public static int[] Snail(int[][] array)
    {
        if (!array.SelectMany(x => x).Any())
            return new int[0];

        int length = array.Length;
        int rowStart = 0, colStart = 0;
        int rowEnd = length - 1, colEnd = length - 1;
        int nSquared = length * length;
        var result = new int[nSquared];
        int index = 0;

        while (index < nSquared)
        {
            for (int j = colStart; j <= colEnd; j++)
                result[index++] = array[rowStart][j];

            rowStart++;

            for (int i = rowStart; i <= rowEnd; i++)
                result[index++] = array[i][colEnd];

            colEnd--;

            for (int j = colEnd; j >= colStart; j--)
                result[index++] = array[rowEnd][j];

            rowEnd--;

            for (int i = rowEnd; i >= rowStart; i--)
                result[index++] = array[i][colStart];

            colStart++;
        }

        return result;
    }
}