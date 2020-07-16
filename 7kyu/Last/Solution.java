/*
Find the last element of the given argument(s).
        Examples

        last(Arrays.asList(1, 2, 3, 4)); // =>  4
        last("xyz");                     // => "z"
        last(1, 2, 3, 4);                // =>  4
        last(new int[]{1, 2, 3, 4});     // =>  4
*/


/*
//import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T> T last(final List<T> list) {
        return list.get(list.size() - 1);
    }

    public static char last(final String string) {
        return string.charAt(string.length() - 1);
    }

    public static <T> T last(final T... list) {
//        return (T) Arrays.asList(list).get(list.length - 1);
        return list[list.length - 1];
    }
}
*/

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T> T last(final List<T> list) {
        return list.stream().reduce((a, b) -> b).orElse(null);
    }

    public static char last(final String string) {
        return string.chars().mapToObj(c -> (char) c).reduce((a, b) -> b).orElse(null);
    }

    public static <T> T last(final T... list) {
        return Arrays.stream(list).reduce((a, b) -> b).orElse(null);
    }
}
