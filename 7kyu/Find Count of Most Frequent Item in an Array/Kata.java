/*
Complete the function to find the count of the most frequent item of an array.
You can assume that input is an array of integers. For an empty array return 0

        input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
        ouptut: 5

        The most frequent number in the array is -1 and it occurs 5 times.
*/

/*
import java.util.HashMap;

public class Kata {
    public static int mostFrequentItemCount(int[] collection) {
        var counter = new HashMap<Integer, Integer>();
        for (int x : collection) {
            if (!counter.containsKey(x)) counter.put(x, 1);
            else counter.put(x, counter.get(x) + 1);
        }
//        return counter.values().stream().mapToInt(i -> i).max().orElse(0);
        return counter.values().stream().max(Integer::compareTo).get();
    }
}
*/

/*
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata {
    public static int mostFrequentItemCount(int[] collection) {
        return (int) IntStream.of(collection).boxed()
                .collect(Collectors.groupingBy(e -> e, Collectors.counting()))
                .entrySet().stream()
                .collect(Collectors.summarizingLong(Map.Entry::getValue)).getMax();
    }
}
*/

import java.util.stream.*;

public class Kata {
    public static int mostFrequentItemCount(int[] collection) {
        return IntStream.of(collection).boxed()
                .collect(Collectors.groupingBy(e -> e, Collectors.summingInt(e -> 1)))
                .values().stream().max(Integer::compare).orElse(0);
    }
}
