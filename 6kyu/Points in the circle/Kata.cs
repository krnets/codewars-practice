/*
using System;
using System.Linq;

public class Kata
{
    public static int pointsNumber(int radius)
    {
        return 4 * (radius + Enumerable.Range(1, radius)
                   .Aggregate(0, (acc, i) =>
                       acc + (int) Math.Sqrt(radius * radius - Math.Pow(i, 2))))
               + 1;
    }
}
*/

using System;
using System.Linq;

public class Kata
{
    public static int pointsNumber(int radius)
    {
        var r2 = radius * radius;

        return 1 + 4 * (Enumerable.Range(0, radius).Sum(i => (int) Math.Sqrt(r2 - i * i)));
    }
}

/*using System;

public class Kata
{
    public static int pointsNumber(int radius)
    {
        int points = 0;
        int r2 = radius * radius;

        for (int i = 0; i < radius; i++)
            points += (int) Math.Sqrt(r2 - i * i);

        return 4 * points + 1;
    }
}*/