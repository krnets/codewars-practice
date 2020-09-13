/*
Simply find the closest value to zero from the list.
Notice that there are negatives in the list.

List is always not empty and contains only integers.
Return None if it is not possible to define only one of such values.
And of course, we are expecting 0 as closest value to zero.

Examples:

        [2, 4, -1, -3]  => -1
        [5, 2, -2]      => None
        [5, 2, 2]       => 2
        [13, 0, -6]     => 0
*/

/*
import java.util.Comparator;
import java.util.stream.IntStream;

public class ClosestToZero {
    public static Integer find(int[] arr) {
        var sorted = IntStream.of(arr).boxed()
                .sorted(Comparator.comparingInt(Math::abs))
                .toArray(Integer[]::new);

        return sorted.length > 1 && sorted[0] != -sorted[1] ? sorted[0] : null;
    }
}

*/

/*
import java.util.stream.IntStream;
import java.util.Comparator;

public class ClosestToZero {
    public static Integer find(int[] arr) {
        int ids = IntStream.range(0, arr.length)
                .boxed()
                .sorted(Comparator.comparingInt(i -> Math.abs(arr[i])))
                .mapToInt(x -> x)
                .limit(2)
                .reduce((x, y) -> Math.abs(arr[x]) == Math.abs(arr[y]) ? -1 : x)
                .getAsInt();

        return ids == -1 ? null : arr[ids];
    }
}
*/

public class ClosestToZero {
    public static Integer find(int[] arr) {
        int closest = Integer.MAX_VALUE;

        for (int x : arr) {
            int a = Math.abs(x);
            int b = Math.abs(closest);

            if (a == b)
                return null;
            if (a < b)
                closest = x;
        }
        return closest;
    }
}

/*
public class ClosestToZero {
    public static Integer find(int[] arr) {
        int closestAbs = Math.abs(arr[0]);
        int closestIndex = 0;
        int count = 1;

        for (int i = 1; i < arr.length; i++) {
            int absX = Math.abs(arr[i]);
            if (absX == closestAbs)
                count++;
            else if (absX < closestAbs) {
                closestAbs = absX;
                closestIndex = i;
                count = 1;
            }
        }
        return count > 1 ? null : arr[closestIndex];
    }
}
*/


/*
import java.util.HashSet;

public class ClosestToZero {
    public static Integer find(int[] arr) {
        var set = new HashSet<Integer>();
        int min = Integer.MAX_VALUE;
        for (int n : arr) {
            if (Math.abs(n) < min) {
                min = Math.abs(n);
                set.clear();
                set.add(n);
            } else if (Math.abs(n) == min) {
                set.add(n);
            }
        }
        return set.size() == 1 ? set.iterator().next() : null;
    }
}*/
