/*using System.Collections.Generic;
using System.Linq;

public class IQ
{
    public static int Test(string numbers)
    {
        var numsList = numbers.Split().Select(int.Parse).ToList();
        var odd = new List<int>();
        var even = new List<int>();

        foreach (int i in numsList)
        {
            if (i % 2 == 0) even.Add(i);
            else odd.Add(i);
        }

        return 1 + numsList.IndexOf(odd.Count == 1 ? odd.ElementAt(0) : even.ElementAt(0));
    }
}*/

using System.Linq;

public class IQ
{
    public static int Test(string numbers)
    {
        int[] numsArray = numbers.Split().Select(int.Parse).ToArray();
        int evenCount = 0, oddCount = 0, lastEvenPos = -1, lastOddPos = -1;

        for (int i = 0; i < numsArray.Length; i++)
        {
            if (numsArray[i] % 2 == 0)
            {
                evenCount++;
                lastEvenPos = i;
            }
            else
            {
                oddCount++;
                lastOddPos = i;
            }

            if (i == 0 || evenCount == 0 || oddCount == 0) continue;
            if (evenCount > oddCount) return 1 + lastOddPos;
            if (oddCount > evenCount) return 1 + lastEvenPos;
        }

        return -1;
    }
}