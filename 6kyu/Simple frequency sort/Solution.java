/*
In this Kata, you will sort elements in an array by decreasing frequency of elements.
If two elements have the same frequency, sort them by increasing value.

        Solution.sortByFrequency(new int[]{ 2, 3, 5, 3, 7, 9, 5, 3, 7 });

        // Returns {3, 3, 3, 5, 5, 7, 7, 2, 9}

        // We sort by highest frequency to lowest frequency.
        // If two elements have same frequency, we sort by increasing value.
*/

/*
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;
import java.util.stream.Collectors;

public class Solution {
    public static int[] sortByFrequency(int[] array) {
        Map<Integer, Long> frequencyMap = Arrays.stream(array).boxed()
                .collect(Collectors.groupingBy(i -> i, Collectors.counting()));

        return Arrays.stream(array).boxed()
                .sorted(Comparator.<Integer, Long>comparing(frequencyMap::get).reversed()
                        .thenComparing(Comparator.naturalOrder()))
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
*/

import java.util.Arrays;
import java.util.stream.Collectors;

public class Solution {
    public static int[] sortByFrequency(int[] array) {
        var list = Arrays.stream(array).boxed().collect(Collectors.toList());
        var freqMap = list.stream().collect(Collectors.groupingBy(i -> i, Collectors.counting()));

        return list.stream().sorted((a, b) -> {
            if (freqMap.get(a).equals(freqMap.get(b))) return a - b;
            else return (int) (freqMap.get(b) - freqMap.get(a));
        }).mapToInt(i -> i).toArray();
    }
}

