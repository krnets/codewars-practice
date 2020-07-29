/*
In your class, you have started lessons about arithmetic progression.
Since you are also a programmer, you have decided to write a function
that will return the first n elements of the sequence with the given
common difference d and first element a.

Note that the difference may be zero!

The result should be a string of numbers, separated by comma and space.

Example
        # first element: 1, difference: 2, how many: 5
        arithmetic_sequence_elements(1, 2, 5) == "1, 3, 5, 7, 9"
*/

import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Progression {
    public static String arithmeticSequenceElements(int first, int step, long total) {
        return IntStream.iterate(first, i -> i + step)
                .limit(total)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining(", "));
    }
}

/*
public class Progression {
    public static String arithmeticSequenceElements(int first, int step, long total) {
        var array = new ArrayList<Integer>();
        for (int i = first; array.size() < total; i += step)
            array.add(i);
        return array.stream().map(String::valueOf).collect(Collectors.joining(", "));
    }
}
*/

/*
public class Progression {
    public static String arithmeticSequenceElements(int first, int step, long total) {
        return IntStream.range(0, (int) total)
                .map(i -> first + i * step)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining(", "));
    }
}

*/
