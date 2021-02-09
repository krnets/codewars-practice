/*using System.Linq;
using static System.Linq.Enumerable;
using static System.String;

public class Kata
{
    public static int TripleDouble(long num1, long num2)
    {
        var strNum1 = num1.ToString();
        var strNum2 = num2.ToString();

        for (int i = 0; i < 10; i++)
        {
            var straightTriple = Concat(Repeat(i, 3).ToList());
            var straightDouble = straightTriple[..2];

            if (strNum1.Contains(straightTriple) && strNum2.Contains(straightDouble))
                return 1;
        }

        return 0;
    }
}*/

public class Kata
{
    public static int TripleDouble(long num1, long num2)
    {
        var strNum1 = num1.ToString();
        var strNum2 = num2.ToString();

        for (char c = '0'; c <= '9'; c++)
        {
            var straightTriple = new string(c, 3);
            var straightDouble = new string(c, 2);

            if (strNum1.Contains(straightTriple) && strNum2.Contains(straightDouble))
                return 1;
        }

        return 0;
    }
}