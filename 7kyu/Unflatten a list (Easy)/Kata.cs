using System;

public class Kata
{
    public static object[] Unflatten(int[] flatArray)
    {
        var output = new object[flatArray.Length];
        int k = 0;

        for (int i = 0; i < flatArray.Length; i++, k++)
            if (flatArray[i] < 3)
                output[k] = flatArray[i];
            else
            {
                int length = Math.Min(flatArray[i], flatArray.Length - i);
                output[k] = flatArray[i..(i + length)];
                i += length - 1;
            }

        return output[..k];
    }
}