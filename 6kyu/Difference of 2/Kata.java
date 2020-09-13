/*
The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

The result array should be sorted in ascending order of values.

Assume there are no duplicate integers in the array.
The order of the integers in the input array should not matter.

Examples

        [1, 2, 3, 4]  should return [[1, 3], [2, 4]]
        [4, 1, 2, 3]  should also return [[1, 3], [2, 4]]
        [1, 23, 3, 4, 7] should return [[1, 3]]
        [4, 3, 1, 5, 6] should return [[1, 3], [3, 5], [4, 6]]
*/


/*
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Kata {
    public static int[][] twosDifference(int[] array) {
        var list = Arrays.stream(array).boxed().sorted().collect(Collectors.toList());
        var pairs = new ArrayList<List<Integer>>();

        for (Integer x : list) {
            if (list.contains(x + 2))
                pairs.add(List.of(x, x + 2));
        }
        var result = new int[pairs.size()][];

        for (int i = 0; i < result.length; i++) {
            result[i] = pairs.get(i).stream().mapToInt(j -> j).toArray();
        }
        return result;
    }
}
*/


/*
import java.util.Arrays;

public class Kata {
    public static int[][] twosDifference(int[] array) {
        return Arrays.stream(array)
                .sorted()
                .filter(i -> Arrays.stream(array).anyMatch(j -> j == i + 2))
                .mapToObj(k -> new int[]{k, k + 2})
                .toArray(int[][]::new);
    }
}*/

/*
import java.util.Arrays;
import java.util.stream.Collectors;

public class Kata {
    public static int[][] twosDifference(int[] array) {
        var list = Arrays.stream(array)
                .sorted()
                .boxed()
                .collect(Collectors.toList());

        return list.stream()
                .filter(v -> list.contains(v + 2))
                .map(v -> new int[]{v, v + 2})
                .toArray(int[][]::new);
    }
}
*/

import java.util.ArrayList;
import java.util.Arrays;

public class Kata {
    public static int[][] twosDifference(int[] array) {
        var listOfArrays = new ArrayList<int[]>();

        Arrays.sort(array);

        for (int i = 0; i < array.length - 1; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] - array[i] == 2)
                    listOfArrays.add(new int[]{array[i], array[j]});
            }
        }
        return listOfArrays.toArray(new int[listOfArrays.size()][]);
    }
}
