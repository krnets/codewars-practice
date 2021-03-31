/*using System.Linq;

public class Kata
{
    public static int Calculate(string str)
    {
        return str.Replace(" ", "").Split("+").Sum(int.Parse);
    }
}*/

using System.Data;
using static System.String;

public class Kata
{
    public static int Calculate(string str)
    {
        return (int) new DataTable().Compute(str.Replace(" ", Empty), Empty);
    }
}