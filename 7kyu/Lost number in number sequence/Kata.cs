using System.Collections.Generic;

public class Kata
{
    public static int FindDeletedNumber(List<int> startingList, List<int> mixedList)
    {
        if (startingList.Count == 0) return 0;
        if (mixedList.Count == 0) return 1;

        mixedList.Sort();

        for (int i = 0; i < mixedList.Count; ++i)
            if (mixedList[i] != startingList[i])
                return startingList[i];

        return 0;
    }
}