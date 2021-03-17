public class StrongestEvenNumber
{
    public static int strongestEven(int n, int m)
    {
        while (n <= (m & m - 1))
            m = m & m - 1;

        return m;
    }
}
