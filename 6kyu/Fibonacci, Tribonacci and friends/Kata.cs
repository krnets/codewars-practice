using System;
using System.Linq;

public class Xbonacci
{
    public double[] xbonacci(double[] signature, int n)
    {
        var arr = new double[n];
        Array.Copy(signature, arr, Math.Min(n, signature.Length));

        for (int i = signature.Length; i < n; i++)
            arr[i] = arr[(i - signature.Length)..i].Sum();

        return arr;
    }
}