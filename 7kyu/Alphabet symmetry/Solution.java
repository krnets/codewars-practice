/*
Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2.
In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy
the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions
in the alphabet for each word. For example,

        solve(["abode","ABc","xyzD"]) = [4, 3, 1]

        See test cases for more examples.

        Input will consist of alphabet characters, both uppercase and lowercase. No spaces.
*/

/*
import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {
    public static int[] solve(String[] arr) {
        var res = new ArrayList<Integer>();
        var abc = IntStream.range(0, 26)
                .mapToObj(i -> Character.toString(i + (int) 'a'))
                .collect(Collectors.joining());

        for (String s : arr)
            res.add((int) IntStream.range(0, Math.min(s.length(), 26))
                    .filter(i -> s.toLowerCase().charAt(i) == abc.charAt(i))
                    .count());

        return res.stream().mapToInt(i -> i).toArray();
    }
}*/

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Solution {
    private static int abcLength = 26;

    private static final String alphabet = IntStream.range(0, abcLength)
            .mapToObj(i -> Character.toString(i + (int) 'a'))
            .collect(Collectors.joining());

    private static int countLetters(String s) {
        return (int) IntStream.range(0, Math.min(s.length(), abcLength))
                .filter(i -> s.charAt(i) == alphabet.charAt(i))
                .count();
    }

    public static int[] solve(String[] arr) {
        return Stream.of(arr).map(String::toLowerCase)
                .mapToInt(Solution::countLetters)
                .toArray();
    }
}
*/

/*
import static java.util.stream.IntStream.range;
import static java.util.stream.Stream.of;
*/

/*
public class Solution {
    public static int[] solve(String[] arr) {
        return of(arr)
                .mapToInt(s -> (int) range(0, s.length()).filter(i -> i == s.toUpperCase().charAt(i) - 65).count())
                .toArray();
    }
}
*/

/*
public class Solution {
    public static int[] solve(String[] arr) {
        int codePointA = (int) 'A';
        return of(arr)
                .mapToInt(s -> (int) range(0, s.length()).filter(i -> i == s.toUpperCase().charAt(i) - codePointA).count())
                .toArray();
    }
}
*/

import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Solution {
    public static int[] solve(String[] arr) {
        return Stream.of(arr).mapToInt(Solution::countLetters).toArray();
    }

    private static int countLetters(String str) {
        return (int) IntStream.range(0, Math.min(str.length(), 26))
                .filter(i -> (i + 'a') == str.toLowerCase().charAt(i))
                .count();
    }
}
