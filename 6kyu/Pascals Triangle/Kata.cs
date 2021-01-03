using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static List<int> PascalsTriangle(int n)
    {
        var triangle = new List<int>();

        for (int row = 0; row < n; row++)
        {
            triangle.Add(1);
            
            for (int k = 1; k <= row; k++)
                triangle.Add(triangle.Last() * (row + 1 - k) / k);
        }

        return triangle;
    }
}