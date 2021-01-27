public class Kata
{
    public static int Collatz(int n)
    {
        int length = 1;

        while (n > 1)
        {
            if (n % 2 == 0)
                n /= 2;
            else n = 3 * n + 1;

            length++;
        }

        return length;
    }
}