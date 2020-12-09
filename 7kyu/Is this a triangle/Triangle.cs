using System;
using System.Linq;

/*public class Triangle
{
    public static bool IsTriangle(int a, int b, int c)
    {
        int longest = Math.Max(Math.Max(a, b), c);
        int sumSides = a + b + c;

        return (sumSides - longest) > longest;
    }
}*/

public class Triangle
{
    public static bool IsTriangle(params int[] sides)
    {
        int longestSide = sides.Max();

        return (sides.Sum() - longestSide) > longestSide;
    }
}