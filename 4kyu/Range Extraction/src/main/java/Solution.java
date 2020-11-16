import java.util.ArrayList;

public class Solution {
    public static String rangeExtraction(int[] arr) {
        var list = new ArrayList<String>();
        int rangeStart = 0;
        int rangeEnd = 0;

        while (rangeStart < arr.length) {
            while (++rangeEnd < arr.length && arr[rangeEnd] - arr[rangeEnd - 1] == 1) ;

            if (rangeEnd - rangeStart > 2) {
                list.add(String.format("%d-%d", arr[rangeStart], arr[rangeEnd - 1]));
                rangeStart = rangeEnd;
            } else {
                for (; rangeStart < rangeEnd; rangeStart++) {
                    list.add(String.valueOf(arr[rangeStart]));
                }
            }
        }
        return String.join(",", list);
    }
}
