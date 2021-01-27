class Kata
{
    public static string BalancedNumber(int number)
    {
        var digits = number.ToString();
        int sum = 0, len = digits.Length;

        //for (int i = 0; i < len - i - 2; i++)
        for (int i = 0; i < (len - 1) / 2; i++)
            sum += digits[i] - digits[len - i - 1];

        return sum == 0 ? "Balanced" : "Not Balanced";
    }
}