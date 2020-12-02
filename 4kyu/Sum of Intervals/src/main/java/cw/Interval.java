/*
package cw;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;

public class Interval {

    public static int sumIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return 0;

        intervals = Arrays.stream(intervals).sorted(Comparator.comparingInt(a -> a[0])).toArray(int[][]::new);

        var widenedIntervalSet = new HashSet<int[]>();

        for (int i = 0; i < intervals.length - 1; i++) {
            if (intervals[i] == null) {
                continue;
            }
            int currMin = intervals[i][0];
            int currMax = intervals[i][1];

            for (int j = i + 1; j < intervals.length; j++) {
                int nextMin = intervals[j][0];
                int nextMax = intervals[j][1];

                if (nextMin > currMax) {
                    break;
                }
                currMax = Math.max(currMax, nextMax);
                intervals[i] = new int[]{currMin, currMax};
                intervals[j] = null;
            }
        }

        for (int[] interval : intervals) {
            if (interval != null) {
                widenedIntervalSet.add(new int[]{interval[0], interval[1]});
            }
        }
        return widenedIntervalSet.stream().mapToInt(a -> a[1] - a[0]).sum();
    }
}
*/

package cw;

import java.util.Arrays;
import java.util.Comparator;

public class Interval {

    public static int sumIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        int sum = 0;
        int min = intervals[0][0];
        int max = intervals[0][1];

        for (int[] interval : intervals) {

            if (min < interval[0] && max >= interval[0]) {
                if (max < interval[1]) {
                    max = interval[1];
                }
            } else if (max < interval[0]) {
                sum += (max - min);
                min = interval[0];
                max = interval[1];
            }
        }
        return sum + (max - min);
    }
}
