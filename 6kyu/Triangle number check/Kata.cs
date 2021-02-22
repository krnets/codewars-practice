/*using System;

public class TriangleNumbers
{
    public static bool isTriangleNumber(long number)
    {
        return Math.Sqrt(number * 8 + 1) % 1 == 0;
    }
}*/

public class TriangleNumbers
{
    public static bool isTriangleNumber(long number)
    {
        long sum = 0, row = 1;

        while (sum < number)
        {
            sum += row;
            row++;
        }

        return sum == number;
    }
}

/*public class TriangleNumbers
{
    public static bool isTriangleNumber(long number)
    {
        for (int row = 1; row <= number; row++)
            number -= row;

        return number == 0;
    }
}*/