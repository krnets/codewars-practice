/*
This time no story, no theory. The examples below show you how to write function accum:

        Examples:

        accum("abcd") -> "A-Bb-Ccc-Dddd"
        accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
        accum("cwAt") -> "C-Ww-Aaa-Tttt"

        The parameter of accum is a string which includes only letters from a..z and A..Z.
*/


import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Accumul {
    public static String accum(String s) {
        List<String> strings = IntStream.range(0, s.length())
                .mapToObj(i -> String.valueOf(s.charAt(i)).repeat(i + 1))
                .map(v -> v.substring(0, 1).toUpperCase() + v.substring(1, v.length()).toLowerCase())
                .collect(Collectors.toList());
        return String.join("-", strings);
    }
}
