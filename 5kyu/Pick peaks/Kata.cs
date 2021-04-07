/*using System.Collections.Generic;

public class PickPeaks
{
    public static Dictionary<string, List<int>> GetPeaks(int[] arr)
    {
        var posList = new List<int>();
        var peaksList = new List<int>();
        int pos = 0;

        for (int i = 1; i < arr.Length; i++)
        {
            if (arr[i - 1] < arr[i])
                pos = i;
            else if (arr[i - 1] > arr[i] && pos != 0)
            {
                posList.Add(pos);
                peaksList.Add(arr[i - 1]);
                pos = 0;
            }
        }

        return new Dictionary<string, List<int>> {{"pos", posList}, {"peaks", peaksList}};
    }
}*/

using System.Collections.Generic;

public class PickPeaks
{
    public static Dictionary<string, List<int>> GetPeaks(int[] arr)
    {
        var posList = new List<int>();
        var peaksList = new List<int>();
        int pos = 0;
        bool isIncreasing = false;

        for (int i = 1; i < arr.Length; i++)
        {
            if (arr[i - 1] < arr[i])
            {
                pos = i;
                isIncreasing = true;
            }
            else if (isIncreasing && arr[i - 1] > arr[i])
            {
                posList.Add(pos);
                peaksList.Add(arr[i - 1]);
                isIncreasing = false;
            }
        }

        return new Dictionary<string, List<int>> {{"pos", posList}, {"peaks", peaksList}};
    }
}