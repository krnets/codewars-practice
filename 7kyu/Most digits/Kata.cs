/*public class Kata
{
    public static int FindLongest(int[] number)
    {
        int longest = 0;

        foreach (var x in number)
            if (x.ToString().Length > longest.ToString().Length)
                longest = x;

        return longest;
    }
}*/

using System.Linq;

public class Kata
{
    public static int FindLongest(int[] number)
    {
        return number.OrderByDescending(x => x.ToString().Length).First();
    }
}