public class DivSeven
{
    public static long[] Seven(long m)
    {
        long steps = 0;

        while (m > 99)
        {
            m = m / 10 - (m % 10) * 2;
            steps++;
        }

        return new[] {m, steps};
    }
}