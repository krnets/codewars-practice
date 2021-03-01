/*using System;

class Kata
{
    public static int SquaresNeeded(long grains)
    {
        return (int) Math.Ceiling(Math.Log2(grains + 1));
    }
}*/

class Kata
{
    public static int SquaresNeeded(long grains)
    {
        return grains == 0 ? 0 : 1 + SquaresNeeded(grains / 2);
    }
}