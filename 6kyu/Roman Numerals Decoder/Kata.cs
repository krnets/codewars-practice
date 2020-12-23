using System.Collections.Generic;

public class RomanDecode
{
    public static int Solution(string roman)
    {
        int sum = 0;
        var map = new Dictionary<char, int> {['M'] = 1000, ['D'] = 500, ['C'] = 100, ['L'] = 50, ['X'] = 10, ['V'] = 5, ['I'] = 1};

        for (int i = 0; i < roman.Length; i++)
            if (i < roman.Length - 1 && map[roman[i]] < map[roman[i + 1]])
                sum -= map[roman[i]];
            else sum += map[roman[i]];

        return sum;
    }
}