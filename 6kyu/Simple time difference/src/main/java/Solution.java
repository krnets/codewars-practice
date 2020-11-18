import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Collectors;

public class Solution {
    public static String solve(String[] arr) {
        int minutesInDay = 24 * 60;
        var diffs = new ArrayList<Integer>();
        var alarms = Arrays.stream(arr)
                .mapToInt(Solution::convertToMinutes)
                .boxed()
                .sorted()
                .collect(Collectors.toList());

        alarms.add(alarms.get(0) + minutesInDay);

        for (int i = 1; i < alarms.size(); i++) {
            diffs.add(alarms.get(i) - alarms.get(i - 1));
        }
        int maxDiff = Collections.max(diffs) - 1;
        int hh = maxDiff / 60;
        int mm = maxDiff % 60;

        return String.format("%02d:%02d", hh, mm);
    }

    private static int convertToMinutes(String s) {
        var split = s.split(":");
        var hours = Integer.parseInt(split[0]);
        var minutes = Integer.parseInt(split[1]);

        return 60 * hours + minutes;
    }
}