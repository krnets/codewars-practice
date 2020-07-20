/*
Write a function called unique that takes an array of integers and returns the array with duplicates removed. It must return the values in the same order as first seen in the given array. Thus no sorting should be done, if 52 appears before 10 in the given array then it should also be that 52 appears before 10 in the returned array.

        Assumptions

        All values given are integers (they can be positive or negative).
        You are given an array but it may be empty.
        They array may have duplicates or it may not.

        Example

        UniqueArray.unique([1, 5, 2, 0, 2, -3, 1, 10])
                        -> [1, 5, 2, 0, -3, 10]
*/

import java.util.stream.IntStream;

public class UniqueArray {
    public static int[] unique(int[] integers) {
        return IntStream.of(integers).distinct().toArray();
    }
}

/*
import java.util.ArrayList;

public class UniqueArray {
    public static int[] unique(int[] integers) {
        var unique = new ArrayList<Integer>();
        for (int x : integers)
            if (!unique.contains(x))
                unique.add(x);
        int[] result = new int[unique.size()];
        for (int i = 0; i < unique.size(); i++)
            result[i] = unique.get(i);
        return result;
    }
}
*/
