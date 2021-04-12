/*using System.Linq;

public class Kata
{
    public static int Calculate(string num1, string num2)
    {
        int n1 = num1.Reverse().Select((c, i) => c == '1' ? 1 << i : 0).Sum();
        int n2 = num2.Reverse().Select((c, i) => c == '1' ? 1 << i : 0).Sum();

        return n1 + n2;
    }
}*/

using System.Linq;

public class Kata
{
    public static int Calculate(string num1, string num2)
    {
        return ToInt32(num1) + ToInt32(num2);
    }

    private static int ToInt32(string num)
    {
        return num.Reverse().Select((c, i) => c == '1' ? 1 << i : 0).Sum();
    }
}