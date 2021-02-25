public class Point
{
    public double X;
    public double Y;

    public Point(double x, double y)
    {
        X = x;
        Y = y;
    }

    public override string ToString()
    {
        return $"({X}, {Y})";
    }

    public override bool Equals(object point)
    {
        // Typechecking
        if (point == null || point.GetType() != GetType())
            return false;

        return ToString() == point.ToString();
    }
}