/*
public class JomoPipi
{
    public static char[][] Shift(char[][] m, int n)
    {
        var rows = m.Length;
        var cols = m[0].Length;
        var array = new char[rows][];

        for (int i = 0; i < rows; i++)
            array[i] = new char[cols];

        for (int i = 0; i < rows * cols; i++)
        {
            array[((i + n) / cols) % rows][(i + n) % cols] = m[i / cols][i % cols];
        }

        return array;
    }
}
*/

using System.Linq;

public class JomoPipi
{
    public static char[][] Shift(char[][] m, int n)
    {
        var chars = m.SelectMany(row => row).ToArray();
        var array = chars.Concat(chars).ToArray();
        var pos = chars.Length - (n % chars.Length);

        for (int i = 0; i < m.Length; i++)
        {
            for (int j = 0; j < m[i].Length; j++)
            {
                m[i][j] = array[pos++];
            }
        }

        return m;
    }
}