/*
In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

// Remove the 3's at indices 0 and 3
// followed by removing a 4 at index 1

        solve([3, 4, 4, 3, 6, 3]); // => [4, 6, 3]
*/

import java.util.ArrayList;
import java.util.Collections;

public class Solution {
    public static int[] solve(int[] arr) {
        var seen = new ArrayList<Integer>();
        for (int i = arr.length - 1; i > -1; i--) {
            if (!seen.contains(arr[i]))
                seen.add(arr[i]);
        }
        Collections.reverse(seen);
        return seen.stream().mapToInt(Integer::intValue).toArray();
    }
}

