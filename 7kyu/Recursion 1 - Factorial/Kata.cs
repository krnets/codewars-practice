public class Recursion
{
    public static ulong Factorial(ulong n)
    {
        checked
        {
            return n == 0 ? 1 : n * Factorial(n - 1);
        }
    }
}