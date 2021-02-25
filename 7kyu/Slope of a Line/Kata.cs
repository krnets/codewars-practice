/*public static class Kata
{
    public static double? GetSlope(Point p1, Point p2)
    {
        if (p1.X == p2.X) return null;

        return (p2.Y - p1.Y) / (p2.X - p1.X);
    }
}*/

public static class Kata
{
    public static double? GetSlope(Point p1, Point p2)
    {
        return p1.X == p2.X ? (double?) null : (p2.Y - p1.Y) / (p2.X - p1.X);
    }
}