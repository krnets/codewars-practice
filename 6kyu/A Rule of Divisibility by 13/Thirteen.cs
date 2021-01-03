public class Thirteen
{
    private static readonly int[] arr = {1, 10, 9, 12, 3, 4};

    public static long Thirt(long n)
    {
        long sum = 0;
        long ans = n;

        for (int i = 0; ans > 0; i++)
        {
            sum += (ans % 10) * arr[i % arr.Length];
            ans /= 10;
        }

        return sum == n ? sum : Thirt(sum);
    }
}