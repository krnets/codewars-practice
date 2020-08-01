/*
Given a grid of size m x n, calculate the total number of rectangles contained in this rectangle.
All integer sizes and positions are counted.

Examples:
        numberOfRectangles(3, 2) == 18
        numberOfRectangles(4, 4) == 100

        Here is how the 3x2 grid works (Thanks to GiacomoSorbi for the idea):

        1 rectangle of size 3x2:

        [][][]
        [][][]

        2 rectangles of size 3x1:

        [][][]

        4 rectangles of size 2x1:

        [][]

        2 rectangles of size 2x2

        [][]
        [][]

        3 rectangles of size 1x2:

        []
        []

        6 rectangles of size 1x1:

        []

        As you can see (1 + 2 + 4 + 2 + 3 + 6) = 18, and is the solution for the 3x2 grid.

        There is a very simple solution to this!
*/

/*
public class Solution {
    public static int numberOfRectangles(int m, int n) {
        return (int) ((m + Math.pow(m, 2)) * (n + Math.pow(n, 2)) / 4);
    }
}*/

/*
import static java.util.stream.IntStream.rangeClosed;

public class Solution {
    public static int numberOfRectangles(int m, int n) {
        return rangeClosed(1, m).sum() * rangeClosed(1, n).sum();
    }
}
*/

/*
public class Solution {
    public static int numberOfRectangles(int m, int n) {
        var result = 0;
        for (int i = m; i > 0; i--)
            for (int j = n; j > 0; j--)
                result += (m - i + 1) * (n - j + 1);
        return result;
    }
}
*/

/*
public class Solution {
    public static int numberOfRectangles(int m, int n) {
        var result = 0;
        for (int i = 0; i <= m; i++)
            for (int j = 0; j <= n; j++)
                result += (m - i) * (n - j);
        return result;
    }
}
*/

public class Solution {
    public static int numberOfRectangles(int m, int n) {
        var result = 0;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                result += i * j;
        return result;
    }
}
