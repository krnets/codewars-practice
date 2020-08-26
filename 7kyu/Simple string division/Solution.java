/*
Given a number in form of a string and an integer k
insert k commas into the string and
determine which of the partitions is the largest.

        solve('1234',1) = 234 because ('1','234') or ('12','34') or ('123','4').
        solve('1234',2) = 34 because ('1','2','34') or ('1','23','4') or ('12','3','4').
        solve('1234',3) = 4
        solve('2020',1) = 202
*/

public class Solution {
    public static long solve(String st, int k) {
        int len = st.length() - k;
        var res = 0L;
        for (int i = 0; i <= st.length() - len; i++) {
            var slice = st.substring(i, i + len);
            res = Math.max(res, Long.parseLong(slice));
        }
        return res;
    }
}

/*
import java.util.regex.Pattern;

public class Solution {
    static long solve(String st, int k) {
        return Pattern.compile("(?=(" + ".".repeat(st.length() - k) + "))")
                .matcher(st)
                .results()
                .map(m -> m.group(1))
                .mapToLong(Long::parseLong)
                .max()
                .getAsLong();
    }
}
*/
