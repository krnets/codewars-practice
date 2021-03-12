using System;
using System.Linq;

public class Bowling
{
    public string BowlingPins(int[] arr)
    {
        var table = new char[4][];
        var pinIndex = 1;

        for (int i = 0; i < table.Length; i++)
        {
            var row = new char[7];
            Array.Fill(row, ' ');
            table[i] = row;
            var buffer = row.Length / 2 - i;

            for (int j = buffer; j < row.Length - buffer; j += 2)
            {
                table[i][j] = arr.Contains(pinIndex) ? ' ' : 'I';
                pinIndex++;
            }
        }

        return string.Join("\n", table.Select(row => string.Concat(row)).Reverse());
    }
}