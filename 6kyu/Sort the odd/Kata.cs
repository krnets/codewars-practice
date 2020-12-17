/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int[] SortArray(int[] array)
    {
        var indexOdd = new List<int>();

        for (int i = 0; i < array.Length; i++)
            if (array[i] % 2 == 1)
                indexOdd.Add(i);

        var oddSorted = array.Where(i => i % 2 == 1).OrderBy(i => i).ToList();
        int skipCount = 0;

        foreach (int i in indexOdd)
        {
            array[i] = oddSorted.Skip(skipCount).First();
            skipCount++;
        }

        return array;
    }
}*/

/*using System.Linq;

public class Kata
{
    public static int[] SortArray(int[] array)
    {
        var oddSorted = array.Where(v => v % 2 == 1).OrderBy(v => v).ToArray();
        int oddIndex = 0;

        for (int i = 0; i < array.Length; i++)
            if (array[i] % 2 == 1)
                array[i] = oddSorted[oddIndex++];

        return array;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int[] SortArray(int[] array)
    {
        var oddSorted = new Queue<int>(array.Where(v => v % 2 == 1).OrderBy(v => v));

        return array.Select(v => v % 2 == 1 ? oddSorted.Dequeue() : v).ToArray();
    }
}