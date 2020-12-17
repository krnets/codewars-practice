using System.Collections.Generic;

public class Line
{
    public static string Tickets(int[] peopleInLine)
    {
        var change = new Dictionary<int, int> {{25, 0}, {50, 0}, {100, 0}};

        foreach (int bill in peopleInLine)
        {
            if (bill == 25)
                change[25]++;
            else if (bill == 50)
            {
                change[50]++;
                change[25]--;
            }
            else if (bill == 100)
            {
                change[100]++;
                change[25]--;
                if (change[50] > 0)
                    change[50]--;
                else
                    change[25] -= 2;
            }

            if (change[25] < 0 || change[50] < 0)
                return "NO";
        }

        return "YES";
    }
}