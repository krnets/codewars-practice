public class Kata
{
    public static object SqrtApproximation(int number)
    {
        int k = 0;

        while (k * k < number)
            k++;

        return k * k == number ? (object) k : (object) new int[] {k - 1, k};
    }
}