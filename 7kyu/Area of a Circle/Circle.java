/*
Complete the function circleArea so that it will return the area of a circle with the given radius.
Round the returned number to two decimal places.
If the radius is not positive or not a number, return false.

        Circle.area(-1485.86);    //returns false
        Circle.area(0);           //returns false
        Circle.area(43.2673);     //returns 5881.25
        Circle.area(68);          //returns 14526.72
*/

public class Circle {
    public static double area(double radius) {
        if (radius <= 0 || Double.isNaN(radius))
            throw new IllegalArgumentException();
        return Math.PI * radius * radius;
    }
}