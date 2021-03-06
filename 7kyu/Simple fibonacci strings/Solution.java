/*
Given that

        f0 = '0'
        f1 = '01'
        f2 = '010' = f1 + f0
        f3 = '01001' = f2 + f1

        You will be given a number and your task is to return the nth fibonacci string. For example:

        solve(2) = '010'
        solve(3) = '01001'
*/

/*
class Solution {
    public static String solve(int n) {
        if (n == 0) return "0";
        if (n == 1) return "01";
        return solve(n - 1) + solve(n - 2);
    }
}*/


import java.util.stream.Stream;

class Solution {
    private static final String F_0 = "0";
    private static final String F_1 = "01";

    public static String solve(int n) {
        return Stream.iterate(new String[]{F_1, F_0}, s -> new String[]{s[0] + s[1], s[0]})
                .limit(n + 1)
                .map(s -> s[1])
                .reduce("", (a, b) -> b);
    }
}
