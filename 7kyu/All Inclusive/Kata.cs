using System;
using System.Collections.Generic;
using System.Linq;

public class Rotations
{
    public static Boolean ContainAllRots(string strng, List<string> arr)
    {
        return Enumerable.Range(0, strng.Length)
            .Select(i => strng[i..] + strng[0..i])
            .All(arr.Contains);
    }
}