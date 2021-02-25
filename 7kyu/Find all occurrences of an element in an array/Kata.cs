/*using System.Collections.Generic;

public class Kata
{
    public static int[] FindAll(int[] array, int n)
    {
        var list = new List<int>();

        for (int i = 0; i < array.Length; i++)
            if (array[i] == n)
                list.Add(i);

        return list.ToArray();
    }
}*/

using System.Linq;

public class Kata
{
    public static int[] FindAll(int[] array, int n)
    {
        return Enumerable.Range(0, array.Length).Where(i => array[i] == n).ToArray();
    }
}