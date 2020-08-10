/*
Below we will define what and n-interesting polygon is and your task is to find its area for a given n.

A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon
and appending 1-interesting polygons to its rim side by side.

Example

        For n = 1, the output should be 1;
        For n = 2, the output should be 5;
        For n = 3, the output should be 13.

Input/Output

        [input] integer n
        Constraints: 1 ≤ n < 10000.

        [output] an integer
        The area of the n-interesting polygon.
*/

/*
public class Kata {
    public static int shapeArea(int n) {
        return (int) (Math.pow(n, 2) + Math.pow(n - 1, 2));
    }
}
*/

/*
public class Kata {
    public static int shapeArea(int n) {
        return 2 * (n * n - n) + 1;
    }
}
*/
public class Kata {
    public static int shapeArea(int n) {
        return (n * (n - 1) << 1) + 1;
    }
}
