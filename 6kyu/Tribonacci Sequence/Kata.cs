/*using System.Collections.Generic;
using System.Linq;

public class Xbonacci
{
    public double[] Tribonacci(double[] signature, int n)
    {
        var list = new List<double>();

        for (int i = 0; i < n; i++)
        {
            if (i < 3)
                list.Add(signature[i]);
            else
                list.Add(list.ElementAt(i - 3) + list.ElementAt(i - 2) + list.ElementAt(i - 1));
        }

        return list.ToArray();
    }
}*/

/*
using System.Collections.Generic;
using System.Linq;

public class Xbonacci
{
    public double[] Tribonacci(double[] signature, int n)
    {
        var list = new List<double>(signature);

        for (int i = 3; i < n; i++)
            list.Add(list.ElementAt(i - 3) + list.ElementAt(i - 2) + list.ElementAt(i - 1));

        return list.ToArray();
    }
}
*/

using System;

public class Xbonacci
{
    public double[] Tribonacci(double[] signature, int n)
    {
        var result = new double[n];
        Array.Copy(signature, result, Math.Min(3, n));

        for (int i = 3; i < n; i++)
            result[i] = result[i - 3] + result[i - 2] + result[i - 1];

        return result;
    }
}