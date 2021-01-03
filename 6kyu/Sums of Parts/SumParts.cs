/*using System.Linq;

class SumParts
{
    public static int[] PartsSums(int[] ls)
    {
        var result = new int[ls.Length + 1];

        for (int i = 0; i < ls.Length; i++)
            result[i] = ls.Skip(i).Sum();

        return result;
    }
}*/

/*
class SumParts
{
    public static int[] PartsSums(int[] ls)
    {
        int sum = 0;
        var result = new int[ls.Length + 1];

        for (int i = ls.Length - 1; i >= 0; i--)
        {
            sum += ls[i];
            result[i] = sum;
        }

        return result;
    }
}
*/

using System.Linq;

class SumParts
{
    public static int[] PartsSums(int[] ls)
    {
        var result = new int[ls.Length + 1];
        int sum = ls.Sum();
        result[0] = sum;

        for (int i = 0; i < ls.Length; i++)
        {
            sum -= ls[i];
            result[i + 1] = sum;
        }

        return result;
    }
}