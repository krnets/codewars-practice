/*using System;
using System.Linq;
using System.Text.RegularExpressions;

public class DirReduction
{
    public static string[] dirReduc(string[] arr)
    {
        var str = string.Join("1", arr);
        var pattern = "NORTH1+SOUTH|EAST1+WEST|WEST1+EAST|SOUTH1+NORTH";

        while (Regex.IsMatch(str, pattern))
            str = Regex.Replace(str, pattern, "");

        return str.Split("1", StringSplitOptions.RemoveEmptyEntries).ToArray();
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class DirReduction
{
    public static string[] dirReduc(string[] arr)
    {
        var stack = new Stack<string>();
        var opposites = new Dictionary<string, string>();
        string[] directions = {"NORTH", "EAST", "SOUTH", "WEST"};
        int n = directions.Length;

        for (int i = 0; i < n; i++)
            opposites.Add(directions[i], directions[(i + 2) % n]);

        foreach (var s in arr)
            if (stack.Count > 0 && opposites[stack.Peek()] == s)
                stack.Pop();
            else stack.Push(s);

        return stack.Reverse().ToArray();
    }
}