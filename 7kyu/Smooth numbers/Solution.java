/*
The concept of "smooth number" is applied to all those numbers
whose prime factors are lesser than or equal to 7:
60 is a smooth number (2 * 2 * 3 * 5), 111 is not (3 * 37).

More specifically, smooth numbers are classified by their highest prime factor
and your are tasked with writing a isSmooth/is_smooth function that
returns a string with this classification as it follows:

        2-smooth numbers should be all defined as a "power of 2", as they are merely that;
        3-smooth numbers are to return a result of "3-smooth";
        5-smooth numbers will be labelled as "Hamming number"s
        7-smooth numbers are classified as "humble numbers"s;
        for all the other numbers, just return non-smooth.

Examples:

        isSmooth(16) == "power of 2"
        isSmooth(36) == "3-smooth"
        isSmooth(60) == "Hamming number"
        isSmooth(98) == "humble number"
        isSmooth(111) == "non-smooth"

The provided input n is always going to be a positive number > 1.
*/

/*
public class Solution {
    public static String isSmooth(long n) {
        for (int i = 2; i < 8; i++) {
            while (n % i == 0) {
                n /= i;
                if (n == 1 && i == 2) return "power of 2";
                if (n == 1 && i == 3) return "3-smooth";
                if (n == 1 && i == 5) return "Hamming number";
                if (n == 1 && i == 7) return "humble number";
            }
        }
        return "non-smooth";
    }
}*/

import java.util.Map;

/*
public class Solution {
    private static final Map<Integer, String> map = Map
            .of(2, "power of 2", 3, "3-smooth", 5, "Hamming number", 7, "humble number");

    public static String isSmooth(long n) {
        for (int i = 2; i < 8; i++) {
            while (n % i == 0) n /= i;
            if (n == 1 && map.containsKey(i))
                return map.get(i);
        }
        return "non-smooth";
    }
}
*/
public class Solution {
    public static String isSmooth(long n) {
        int k = 2;
        while (n != 1) {
            if (n % k == 0)
                n /= k;
            else k++;
        }
        return Map.of(2, "power of 2", 3, "3-smooth", 5, "Hamming number", 7, "humble number")
                .getOrDefault(k, "non-smooth");
    }
}
