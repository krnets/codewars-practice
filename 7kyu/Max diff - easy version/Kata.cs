public class kata
{
    public static int maxDiff(int[] lst)
    {
        int min = int.MaxValue;
        int max = int.MinValue;

        foreach (var i in lst)
        {
            if (min > i) min = i;
            if (max < i) max = i;
        }

        return lst.Length == 0 ? 0 : max - min;
    }
}