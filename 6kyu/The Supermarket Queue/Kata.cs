/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static long QueueTime(int[] customers, int n)
    {
        var tills = new List<int>(new int[n]);

        foreach (int c in customers)
        {
            int shortest = tills.Min();
            tills[tills.IndexOf(shortest)] = shortest + c;
        }

        return tills.Max();
    }
}*/

/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static long QueueTime(int[] customers, int n)
    {
        var registers = new List<int>(Enumerable.Repeat(0, n));

        foreach (int customer in customers)
            registers[registers.IndexOf(registers.Min())] += customer;

        return registers.Max();
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static long QueueTime(int[] customers, int n)
    {
        var tills = new int[n];

        foreach (int customer in customers)
            tills[Array.IndexOf(tills, tills.Min())] += customer;

        return tills.Max();
    }
}