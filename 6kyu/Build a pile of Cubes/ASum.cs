/*public class ASum
{
    public static long findNb(long m)
    {
        long n = 1, cubeLevelsSum = 0;

        while (cubeLevelsSum < m)
        {
            cubeLevelsSum += (n * n * n);
            n++;
        }

        return cubeLevelsSum == m ? n - 1 : -1;
    }
}*/

public class ASum
{
    public static long findNb(long m)
    {
        long n = 0;

        while (m > 0)
        {
            n++;
            m -= (n * n * n);
        }

        return m == 0 ? n : -1;
    }
}