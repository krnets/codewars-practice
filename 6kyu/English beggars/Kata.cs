public class Kata
{
    public static int[] Beggars(int[] values, int n)
    {
        var result = new int[n];

        for (int i = 0; n > 0 && i < values.Length; i++)
            result[i % n] += values[i];

        return result;
    }
}