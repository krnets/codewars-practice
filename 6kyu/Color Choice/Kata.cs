public class CheckChoose
{
    public static long Checkchoose(long m, int n)
    {
        long c = 1;

        for (long i = 1; i <= n; i++)
        {
            c = c * (n - i + 1) / i;

            if (c == m)
                return i;
        }

        return -1L;
    }
}