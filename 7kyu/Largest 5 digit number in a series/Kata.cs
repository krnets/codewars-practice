using System;

public class Kata
{
    public static int GetNumber(string str)
    {
        int largest = Int32.MinValue;

        for (int i = 0; i < str.Length - 4; i++)
            largest = Math.Max(largest, int.Parse(str.Substring(i, 5)));

        return largest;
    }
}