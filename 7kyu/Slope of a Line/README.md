### Slope of a Line

Your challenge is to write a function named GetSlope that calculates the slope of the line through two points.
Input

GetSlope will take in two Point objects. If the line through the two points is vertical, or the two points are the same, return null.

The Point object:
```c
public class Point
{
  public double X;
  public double Y;

  public Point(double x, double y)
  {
    this.X = x;
    this.Y = y;
  }

  public override string ToString()
  {
    return $"({this.X}, {this.Y})";
  }

  public override bool Equals(object point)
  {
    // Typechecking
    if (point == null || point.GetType() != this.GetType())
    {
      return false;
    }

    return this.ToString() == point.ToString();
  }
}
