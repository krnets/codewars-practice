using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public int SumGroups(int[] arr)
    {
        var str = string.Concat(arr.Select(x => $"{x % 2}"));
        str = Regex.Replace(str, "1(11)*", "1");
        str = Regex.Replace(str, "(0|11)+", "0");

        return str.Length;
    }
}


/*using System.Collections.Generic;

public class Kata
{
    public int SumGroups(int[] arr)
    {
        var list = new List<int>();
        int groupSum = arr[0], flag = 0;

        for (int i = 1; i < arr.Length; i++)
        {
            if (arr[i - 1] % 2 != arr[i] % 2)
            {
                list.Add(groupSum);
                groupSum = 0;
            }
            else flag = 1;

            groupSum += arr[i];
        }

        list.Add(groupSum);

        return flag == 0 ? list.Count : SumGroups(list.ToArray());
    }
}*/