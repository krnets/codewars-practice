public class Kata
{
    public int[] Withdraw(int n)
    {
        var denom = new[] {100, 50, 20};
        var bills = new[] {0, 0, 0};

        while (n % denom[1] > 0)
        {
            n -= denom[2];
            bills[2]++;
        }

        bills[1] = (n % denom[0]) / denom[1];
        bills[0] = n / denom[0];

        return bills;
    }
}