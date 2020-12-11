using System;
using System.Collections.Generic;

public class Kata
{
    public static int Number(List<int[]> peopleListInOut)
    {
        int passengers = 0;

        foreach (var busStop in peopleListInOut)
        {
            passengers -= busStop[1];

            if (passengers < 0)
                throw new Exception("number of remaining passengers cannot be negative");

            passengers += busStop[0];
        }

        return passengers;
    }
}