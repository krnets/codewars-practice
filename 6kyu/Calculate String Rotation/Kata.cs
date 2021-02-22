/*public class CalculateStringRotation
{
    public static int ShiftedDiff(string first, string second)
    {
        for (int i = 0; i < first.Length; i++)
        {
            if (first.Equals(second))
                return i;

            first = first[^1] + first[..^1];
        }

        return -1;
    }
}*/

public class CalculateStringRotation
{
    public static int ShiftedDiff(string first, string second)
    {
        return first.Length != second.Length
            ? -1
            : string.Join("", second, second).IndexOf(first);
    }
}