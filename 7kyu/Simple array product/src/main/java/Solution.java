import java.util.ArrayList;
import java.util.Collections;

public class Solution {

    public static int solve(int[][] arr) {
        int max = 1;
        int min = 1;

        for (int[] ints : arr) {
            var list = new ArrayList<Integer>();

            for (int x : ints) {
                list.add(x * max);
                list.add(x * min);
            }
            max = Collections.max(list);
            min = Collections.min(list);
        }
        return max;
    }
}