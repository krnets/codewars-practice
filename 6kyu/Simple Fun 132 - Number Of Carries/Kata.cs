/*public class Kata
{
    public int NumberOfCarries(int a, int b)
    {
        int carry = 0;
        int count = 0;

        while (a > 0 || b > 0)
        {
            if ((a % 10 + b % 10 + carry) > 9)
            {
                carry = 1;
                count++;
            }
            else carry = 0;

            a /= 10;
            b /= 10;
        }

        return count;
    }
}*/

public class Kata
{
    public int NumberOfCarries(int a, int b)
    {
        int carry = 0, count = 0;

        while (a > 0 || b > 0)
        {
            carry = a % 10 + b % 10 + carry / 10;

            if (carry > 9)
                count++;

            a /= 10;
            b /= 10;
        }

        return count;
    }
}