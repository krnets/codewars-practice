using System.Linq;

public class WeightSort
{
    public static string orderWeight(string strng)
    {
        return string.Join(" ", strng.Split().OrderBy(s => s.Sum(char.GetNumericValue)).ThenBy(s => s));
    }
}