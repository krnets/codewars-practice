/*
You are given an array (which will have a length of at least 3, but could be very large)
containing integers. The array is either entirely comprised of odd integers or entirely
comprised of even integers except for a single integer N.

Write a method that takes the array as an argument and returns this "outlier" N.

        [2, 4, 0, 100, 4, 11, 2602, 36]
        Should return: 11 (the onl  y odd number)

        [160, 3, 1719, 19, 11, 13, -21]
        Should return: 160 (the only even number)
*/

/*
import java.util.ArrayList;

public class FindOutlier {
    static int find(int[] integers) {
        var odd = new ArrayList<Integer>();
        var even = new ArrayList<Integer>();
        for (int x : integers) {
            if (x % 2 == 0) even.add(x);
            else odd.add(x);
        }
        return odd.size() == 1 ? odd.get(0) : even.get(0);
    }
}
*/


import static java.util.Arrays.stream;

/*
public class FindOutlier {
    static int find(int[] integers) {
        var sum = stream(integers).limit(3).map(x -> Math.abs(x) % 2).sum();
        var mod = sum < 2 ? 1 : 0;
        return stream(integers).filter(x -> Math.abs(x) % 2 == mod).findFirst().orElse(0);
    }
}
*/
public class FindOutlier {
    static int find(int[] integers) {
        var p = stream(integers).limit(3).map(x -> Math.abs(x) % 2).sum() / 2;
        return stream(integers).filter(x -> Math.abs(x) % 2 != p).findFirst().orElse(0);
    }
}
