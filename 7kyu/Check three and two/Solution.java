
/*
Given an array with exactly 5 strings "a", "b" or "c" (chars in Java),
check if the array contains three and two of the same values.

Examples:
        ["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
        ["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
        ["a", "a", "a", "a", "a"] ==> false // 5x "a"
*/

/*
import java.util.HashMap;

public class Solution {
    public boolean checkThreeAndTwo(char[] chars) {
        var counter = new HashMap<Character, Integer>();
        for (char c : chars) {
            if (!counter.containsKey(c))
                counter.put(c, 1);
            else
                counter.put(c, counter.get(c) + 1);
        }
        return counter.values().contains(2) && counter.values().contains(3);
    }
}
*/

import java.util.*;
import static java.util.function.Function.identity;
import static java.util.stream.Collectors.*;

public class Solution {
    public boolean checkThreeAndTwo(char[] chars) {
        return Arrays.toString(chars)
                .chars()
                .boxed()
                .collect(groupingBy(identity(), counting()))
                .values()
                .containsAll(Set.of(2L, 3L));
    }
}
