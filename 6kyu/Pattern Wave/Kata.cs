/*using System.Linq;

public class Kata
{
    public static string Draw(int[] waves)
    {
        var rows = waves.Max();
        var table = new char[rows][];

        for (int i = 0; i < rows; i++)
        {
            table[i] = new char[waves.Length];

            for (int j = 0; j < waves.Length; j++)
            {
                if (waves[j] > 0)
                {
                    table[i][j] = '■';
                    waves[j]--;
                }
                else table[i][j] = '□';
            }
        }

        return string.Join("\n", Enumerable.Range(0, rows).Select(i => string.Concat(table[i])).Reverse());
    }
}*/

using System.Linq;

public class Kata
{
    public static string Draw(int[] waves)
    {
        return string.Join("\n", Enumerable.Range(0, waves.Max())
            .Select(i => string.Concat(waves.Select(w => w > i ? '■' : '□'))).Reverse());
    }
}