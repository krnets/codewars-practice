/*using System;

public class Kata
{
    public static char FindMissingLetter(char[] array)
    {
        for (int i = 1; i < array.Length; i++)
            if (array[i] - array[i - 1] != 1)
                return (char) (array[i - 1] + 1);

        throw new Exception("no missing letters found");
    }
}*/

using System.Linq;

public class Kata
{
    public static char FindMissingLetter(char[] array)
    {
        return Enumerable.Range(array[0], array.Length).Select(i => (char) i).Except(array).Single();
    }
}