using System.Collections.Generic;

public class Deadfish
{
    public static int[] Parse(string data)
    {
        var list = new List<int>();
        int val = 0;

        foreach (char c in data)
            switch (c)
            {
                case 'i': val++; break;
                case 'd': val--; break;
                case 's': val *= val; break;
                case 'o': list.Add(val); break;
            }

        return list.ToArray();
    }
}