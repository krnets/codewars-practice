using System.Text;

public class BinaryNumbers
{
    public static string Add(string a, string b)
    {
        var sb = new StringBuilder();
        int sum = BinaryToInt(a) + BinaryToInt(b);

        while (sum > 0)
        {
            sb.Insert(0, sum % 2);
            sum /= 2;
        }

        return sb.Length > 0 ? sb.ToString() : "0";
    }

    private static int BinaryToInt(string str)
    {
        int sum = 0, bit = 1, n = int.Parse(str);

        while (n != 0)
        {
            sum += n % 10 == 1 ? bit : 0;
            bit <<= 1;
            n /= 10;
        }

        return sum;
    }
}