using System.Linq;

public class stringArrayMethods
{
    public static double[] ToDoubleArray(string[] stringArray)
    {
        return stringArray.Select(double.Parse).ToArray();
    }
}