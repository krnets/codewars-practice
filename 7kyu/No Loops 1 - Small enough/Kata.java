/*
You will be given an array and a limit value.
You must check that all values in the array are below or equal to the limit value.
If they are, return true. Else, return false.

You can assume all values in the array are numbers.
*/

import java.util.stream.IntStream;

/*
public class Kata {
    public static boolean smallEnough(int[] a, int limit) {
        return IntStream.of(a).allMatch(v -> v <= limit);
    }
}*/
public class Kata {
    public static boolean smallEnough(int[] a, int limit) {
        return IntStream.of(a).noneMatch(v -> v > limit);
    }
}

/*
public class Kata {
    public static boolean smallEnough(int[] a, int limit) {
        return IntStream.of(a).max().orElse(0) <= limit;
    }
}
*/
