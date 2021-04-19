using System.Collections.Generic;

public class Kata
{
    public static int SevenSegmentNumber(int number)
    {
        if (number < 0 || number > 9)
            throw new System.Exception();

        var segments = new Dictionary<int, int>
        {
            [0] = 0b111_1101, [1] = 0b101_0000,
            [2] = 0b011_0111, [3] = 0b101_0111,
            [4] = 0b101_1010, [5] = 0b100_1111,
            [6] = 0b110_1111, [7] = 0b101_0001,
            [8] = 0b111_1111, [9] = 0b101_1111
        };

        return segments[number];
    }
}