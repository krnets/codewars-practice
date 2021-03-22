public class Kata
{
    public static int GetLastDigit(int index)
    {
        int a = 0, b = 1;

        while (index-- > 0)
            (a, b) = (b, (a + b) % 10);

        return a;
    }
}