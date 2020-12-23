using System.Collections.Generic;

public class SqInRect
{
    public static List<int> sqInRect(int lng, int wdth)
    {
        if (lng == wdth) return null;
        
        var squares = new List<int>();

        while (lng * wdth > 0)
        {
            if (lng > wdth)
            {
                squares.Add(lng - (lng - wdth));
                lng -= wdth;
            }
            else
            {
                squares.Add(wdth - (wdth - lng));
                wdth -= lng;
            }
        }

        return squares;
    }
}