/*
using System;
using System.Linq;

public class DeltaBits
{
    public static int ConvertBits(int a, int b)
    {
        return Convert.ToString(a ^ b, 2).Count(c => c == '1');
    }
}
*/

using System.Collections;
using System.Linq;

public class DeltaBits
{
    public static int ConvertBits(int a, int b)
    {
        return new BitArray(new[] {a ^ b}).Cast<bool>().Count(x => x);
    }
}