/*using System.Linq;

public class Kata
{
    public static int? MaxRedigit(int num)
    {
        return num > 99 && num < 1000
            ? int.Parse(string.Concat(num.ToString()
                .OrderByDescending(x => x)))
            : (int?) null;
    }
}*/

using System.Linq;

public class Kata
{
    public static int? MaxRedigit(int num)
    {
        if (num < 100 || num > 999) return null;

        return int.Parse(string.Concat(num.ToString().OrderByDescending(x => x)));
    }
}