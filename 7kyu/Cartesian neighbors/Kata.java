/*
The сoordinates of a point in the grid are written as (x,y).
Each point in a coordinate system has eight neighboring points.
Provided that the grid step = 1.

It is necessary to write a function that takes a coordinate on the x-axis and y-axis
and returns a list of all the neighboring points.
Points inside list don't have to been sorted (any order is valid).

For Example:
        cartesianNeighbor(2,2) -> {{1,1},{1,2},{1,3},{2,1},{2,3},{3,1},{3,2},{3,3}}
        cartesianNeighbor(5,7) -> {{6,7},{6,6},{6,8},{4,7},{4,6},{4,8},{5,6},{5,8}}
*/

/*
public class Kata {
    public static int[][] cartesianNeighbor(int x, int y) {
        return new int[][]{
                {x - 1, y - 1},
                {x - 1, y},
                {x - 1, y + 1},
                {x, y - 1},
                {x, y + 1},
                {x + 1, y - 1},
                {x + 1, y},
                {x + 1, y + 1}
        };
    }
}*/

import static java.util.stream.IntStream.rangeClosed;

public class Kata {
    public static int[][] cartesianNeighbor(int x, int y) {
        return rangeClosed(x - 1, x + 1)
                .boxed()
                .flatMap(a -> rangeClosed(y - 1, y + 1)
                        .mapToObj(b -> new int[]{a, b}))
                .filter(p -> p[0] != x || p[1] != y)
                .toArray(int[][]::new);
    }
}
