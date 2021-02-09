/*
using System;

public class Kata
{
    public static Tuple<int, int> MineLocation(int[,] field)
    {
        var n = (int) Math.Sqrt(field.Length);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                if (field[i, j] == 1)
                    return new Tuple<int, int>(i, j);
        }

        return new Tuple<int, int>(-1, -1);
    }
}
*/

using System;

public class Kata
{
    public static Tuple<int, int> MineLocation(int[,] field)
    {
        for (int i = 0; i < field.GetLength(0); i++)
        {
            for (int j = 0; j < field.GetLength(1); j++)
                if (field[i, j] == 1)
                    // return new Tuple<int, int>(i, j);
                    return Tuple.Create(i, j);
        }

        // return new Tuple<int, int>(-1, -1);
        return Tuple.Create(-1, -1);
    }
}