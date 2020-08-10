/*
In this Kata, you will be given a string and two indexes (a and b).
Your task is to reverse the portion of that string between those two indices inclusive.

        solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa".
        So we reverse them.
        solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.

        Input will be lowercase and uppercase letters only.

        The first index a will always be lower that than the string length;
        the second index b can be greater than the string length.

*/

/*
public class Solution {
    public static String solve(String s, int a, int b) {
        if (b + 1 > s.length())
            b = s.length() - 1;
        var sb = new StringBuilder(s.substring(a, b + 1));
        return s.substring(0, a) + sb.reverse() + s.substring(b + 1);
    }
}*/

public class Solution {
    public static String solve(String s, int a, int b) {
        b = ++b > s.length() ? s.length() : b;
        var sb = new StringBuilder(s.substring(a, b));
        return s.substring(0, a) + sb.reverse() + s.substring(b);
    }
}