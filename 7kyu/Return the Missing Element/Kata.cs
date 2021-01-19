/*using System;
using System.Linq;

public static class Kata
{
    public static int GetMissingElement(int[] superImportantArray)
    {
        return Enumerable.Range(0, 10).First(x => !superImportantArray.Contains(x));
    }
}*/

/*using System.Linq;

public static class Kata
{
    public static int GetMissingElement(int[] superImportantArray)
    {
        return Enumerable.Range(0, 10).Sum() - superImportantArray.Sum();
    }
}*/

/*using System.Linq;

public static class Kata
{
    public static int GetMissingElement(int[] superImportantArray)
    {
        //return Enumerable.Range(0, 10).Except(superImportantArray).FirstOrDefault();
        return Enumerable.Range(0, 10).Except(superImportantArray).Single();
    }
}*/

public static class Kata
{
    public static int GetMissingElement(int[] superImportantArray)
    {
        int result = 0;

        for (int i = 0; i < 10; i++)
            result ^= i;

        foreach (int x in superImportantArray)
            result ^= x;

        return result;
    }
}